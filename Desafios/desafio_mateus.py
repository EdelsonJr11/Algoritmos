saldo = 2000
def olhar_saldo():
    print(f"Teu saldo é {saldo}R$")

def depositar(saldo):
    deposito = int(input("Quer depositar quanto fi?"))
    return saldo + deposito

def sacar(saldo):
    saque = int(input("Quer sacar quanto fi?"))
    if saque > saldo:
        print(" valeu, bacen! Quer fabricar dinheiro?")
    else:
        return saldo - saque

while True:

    print(f"Bem-Vindo ao Banco do Edelson do Brasi teu saldo é {saldo}R$\n 1. Vericar saldo\n 2. Depositar\n 3. Sacar\n 4. Sair")
    opcao = int(input("Digite o número da opção desejada: "))
    if opcao == 4:
        break
    elif opcao == 1:
        olhar_saldo()
    elif opcao == 2:
        saldo = depositar(saldo)
    elif opcao == 3:
        saldo = sacar(saldo)
    else:
        print("Escolhe uma que tem!")
