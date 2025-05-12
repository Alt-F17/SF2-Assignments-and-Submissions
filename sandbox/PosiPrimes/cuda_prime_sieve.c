#include <cuda_runtime.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <pthread.h>
#include <math.h>

typedef uint8_t BYTE;
typedef uint64_t LONG;
typedef int32_t INT;

#define THREADS_PER_BLOCK 256

typedef struct {
    LONG start;
    LONG end;
    INT segment_id;
} ThreadArgs;

INT *amorce_primes;
INT amorce_count;
BYTE *mask;
LONG mask_size;

#define CUDA_CHECK(err) do { \
    if (err != cudaSuccess) { \
        fprintf(stderr, "CUDA Error: %s (code %d) at %s:%d\n", cudaGetErrorString(err), err, __FILE__, __LINE__); \
        exit(EXIT_FAILURE); \
    } \
} while (0)

void generate_amorce(LONG max_value) {
    LONG limit = (LONG)sqrt((double)max_value);
    BYTE *sieve = (BYTE *)calloc(limit + 1, sizeof(BYTE));
    if (!sieve) {
        perror("Failed to allocate sieve");
        exit(EXIT_FAILURE);
    }

    for (LONG i = 2; i <= limit; i++) {
        if (!sieve[i]) {
            for (LONG j = i * i; j <= limit; j += i) {
                sieve[j] = 1;
            }
        }
    }

    amorce_count = 0;
    for (LONG i = 2; i <= limit; i++) {
        if (!sieve[i]) amorce_count++;
    }

    amorce_primes = (INT *)malloc(amorce_count * sizeof(INT));
    if (!amorce_primes) {
        perror("Failed to allocate amorce_primes");
        exit(EXIT_FAILURE);
    }

    INT idx = 0;
    for (LONG i = 2; i <= limit; i++) {
        if (!sieve[i]) amorce_primes[idx++] = (INT)i;
    }

    free(sieve);
}

void generate_mask(LONG segment_size) {
    mask_size = segment_size / 2;
    mask = (BYTE *)calloc(mask_size, sizeof(BYTE));
    if (!mask) {
        perror("Failed to allocate mask");
        exit(EXIT_FAILURE);
    }

    for (INT i = 0; i < amorce_count; i++) {
        LONG p = amorce_primes[i];
        LONG start = (p - 1) / 2;
        for (LONG j = start; j < mask_size; j += p) {
            mask[j] = 1;
        }
    }
}

__global__ void sieve_kernel(BYTE *d_segment, LONG start, LONG size, INT *d_primes, INT num_primes) {
    LONG idx = blockIdx.x * blockDim.x + threadIdx.x;
    if (idx >= size) return;

    LONG num = start + idx * 2 + 1;
    for (INT i = 0; i < num_primes; i++) {
        LONG p = d_primes[i];
        if (p * p > num) break;
        if (num % p == 0) {
            d_segment[idx] = 1;
            break;
        }
    }
}

void cuda_sieve_segment(BYTE *segment, LONG start, LONG end, size_t segment_size) {
    BYTE *d_segment;
    INT *d_primes;
    size_t byte_size = segment_size * sizeof(BYTE);

    CUDA_CHECK(cudaMalloc(&d_segment, byte_size));
    CUDA_CHECK(cudaMalloc(&d_primes, amorce_count * sizeof(INT)));

    CUDA_CHECK(cudaMemcpy(d_primes, amorce_primes, amorce_count * sizeof(INT), cudaMemcpyHostToDevice));
    CUDA_CHECK(cudaMemset(d_segment, 0, byte_size));

    INT blocks = (segment_size + THREADS_PER_BLOCK - 1) / THREADS_PER_BLOCK;
    sieve_kernel<<<blocks, THREADS_PER_BLOCK>>>(d_segment, start, segment_size, d_primes, amorce_count);
    CUDA_CHECK(cudaGetLastError());
    CUDA_CHECK(cudaDeviceSynchronize());

    CUDA_CHECK(cudaMemcpy(segment, d_segment, byte_size, cudaMemcpyDeviceToHost));

    CUDA_CHECK(cudaFree(d_segment));
    CUDA_CHECK(cudaFree(d_primes));
}

int is_positional(LONG prime, LONG position) {
    char prime_str[20];
    char pos_str[20];
    snprintf(prime_str, sizeof(prime_str), "%lu", prime);
    snprintf(pos_str, sizeof(pos_str), "%lu", position);
    return strstr(prime_str, pos_str) != NULL;
}

void *process_segment(void *arg) {
    ThreadArgs *args = (ThreadArgs *)arg;
    LONG start = args->start;
    LONG end = args->end;
    INT segment_id = args->segment_id;

    size_t segment_size = (end - start) / 2;
    BYTE *segment = (BYTE *)calloc(segment_size, sizeof(BYTE));
    if (!segment) {
        perror("Failed to allocate segment");
        pthread_exit(NULL);
    }

    cuda_sieve_segment(segment, start, end, segment_size);

    FILE *fp = fopen("primes.txt", "a");
    if (!fp) {
        perror("Failed to open primes.txt");
        free(segment);
        pthread_exit(NULL);
    }

    LONG position = start;
    for (LONG i = 0; i < segment_size; i++) {
        LONG num = start + i * 2 + 1;
        if (!segment[i] && !mask[i % mask_size]) {
            position++;
            if (is_positional(num, position)) {
                fprintf(fp, "Segment %d: %lu at position %lu\n", segment_id, num, position);
            }
        }
    }

    fclose(fp);
    free(segment);
    free(args);
    pthread_exit(NULL);
}

int main(int argc, char *argv[]) {
    if (argc < 3) {
        fprintf(stderr, "Usage: %s <max_value> <num_threads>\n", argv[0]);
        return 1;
    }

    LONG max_value = atoll(argv[1]);
    INT num_threads = atoi(argv[2]);

    CUDA_CHECK(cudaSetDevice(0));

    size_t free_mem, total_mem;
    CUDA_CHECK(cudaMemGetInfo(&free_mem, &total_mem));
    size_t usable_mem = total_mem * 0.95; // again, minecraft

    generate_amorce(max_value);
    LONG segment_size = usable_mem / (num_threads * sizeof(BYTE) * 2);
    generate_mask(segment_size * 2);

    LONG num_segments = (max_value / (segment_size * 2)) + 1;
    pthread_t *threads = (pthread_t *)malloc(num_threads * sizeof(pthread_t));
    INT active_threads = 0;

    for (LONG i = 0; i < num_segments; i++) {
        LONG start = i * segment_size * 2 + 1;
        LONG end = start + segment_size * 2;
        if (end > max_value) end = max_value;

        ThreadArgs *args = (ThreadArgs *)malloc(sizeof(ThreadArgs));
        args->start = start;
        args->end = end;
        args->segment_id = i;

        pthread_create(&threads[active_threads], NULL, process_segment, args);
        active_threads++;

        if (active_threads == num_threads || i == num_segments - 1) {
            for (INT j = 0; j < active_threads; j++) {
                pthread_join(threads[j], NULL);
            }
            active_threads = 0;
        }
    }

    free(threads);
    free(amorce_primes);
    free(mask);
    CUDA_CHECK(cudaDeviceReset());

    return 0;
}