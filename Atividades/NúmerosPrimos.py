def checarPrimo():
    n = int(input("Digite um número:"))
    if n < 2:
        print(n, "não é primo")
        return
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print(f"{n} não é primo")
            return
    print(f"{n} é primo")

def quantidadePrimos():
    quant = int(input("Quer saber quantos primos existem até qual número? "))
    cont = 0
    for n in range(2, quant + 1):
        is_primo = True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                is_primo = False
                break
        if is_primo:
            cont += 1
    print(f"Existem {cont} números primos até {quant}.")

while True:
    opcao = int(input("1.checar se é primo\n2.quantidade de números primos\n3.sair\n"))
    if opcao == 3:
        break
    elif opcao == 1:
        checarPrimo()
    elif opcao == 2:
        quantidadePrimos()