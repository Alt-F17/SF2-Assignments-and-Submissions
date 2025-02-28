def binom(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return binom(n-1, k-1) + binom(n-1, k)

def pascal_print(n):
    for row in range(n):
        for k in range(row+1):
            print(binom(row, k), end=' ')
        print()

pascal_print(int(input("Enter the number of rows: ")))