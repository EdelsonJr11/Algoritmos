def soma(x, y):
    print(x + y)
    print("Soma de três pares de números:")

soma(1, 2)
soma(3, 4)
soma(5, 6)

def subtracao(x, y):
    print(x - y)
print("Subtração de três pares de números:")

subtracao(10, 5)
subtracao(20, 15)
subtracao(30, 25)

def multiplicacao(x, y):
    print(x * y)
print("Multiplição de três pares de números:")

multiplicacao(2, 3)
multiplicacao(4, 5)
multiplicacao(6, 7)


def divisao(x, y):
    print(x / y)
print("Divisão de três pares de números:")

divisao(10, 2)
divisao(20, 4)
divisao(20, 4)

def potencia(x, y):
    print(x ** y)
print("Potência de três pares de números:")

potencia(2, 3)
potencia(3, 2)
potencia(4, 2)

def fatorial(n):
    r = 1
    for i in range(n, 1, -1):
        r *= i
    return r
print("Fatorial de três pares de números:")

print(fatorial(5))
print(fatorial(6))
print(fatorial(7))