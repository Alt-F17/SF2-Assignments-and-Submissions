import sympy

n = 3
for i in range(int(input("Enter the number of iterations: "))):
    if sympy.isprime(n):
        prepend = 1
        while True:
            new_n = int(str(prepend) + str(n))
            if sympy.isprime(new_n):
                n = new_n
                break
            prepend += 1
    print(n)