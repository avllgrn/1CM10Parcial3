import os

def fibonacci(n):
    a = 0
    b = 1

    if n==0 or n==1:
        return n
    elif n>1:
        i=2         # Contador en rango [2, n]
        while i<=n:
            c = a+b
            a=b
            b=c
            i = i+1
        return c

if __name__ == '__main__':
    os.system('cls')

    n = int(input('Ingresa n '))
    print()

    f = fibonacci(n)
    print(f'fibonacci({n}) = {f}')
    print()
