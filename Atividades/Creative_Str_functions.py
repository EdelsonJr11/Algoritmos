def AddMotors():
    if not motos:
        entrada = (input("Digite o nome da moto "))
        motos.append(", ".join(entrada.split()).title().strip())
        print("Moto adicionada!")

    print(f"Motos que você já tem: {', '.join(motos)}")
    confirmacao = input("Quer adicionar mais?(s ou n) ").lower()

    while confirmacao == 's':
        entrada = (input("Digite o nome da moto "))
        motos.append(", ".join(entrada.split()).title())
        print("Moto adicionada!")

        confirmacao = input("Quer adicionar mais?(s ou n) ").lower()

    if confirmacao == 'n':
        return

    else:
        ("s ou n cavalo")


def AddCar():
    if not cars:
        entrada = input("Digite o nome do carro ")
        cars.append(", ".join(entrada.split()).title())
        print("Carro adicionado!")

    print(f"Carros que você já tem: {', '.join(cars)}")
    confirmacao = input("Quer adicionar mais?(s ou n) ").lower()

    while confirmacao == 's':
        entrada = input("Digite o nome do carro ")
        cars.append(", ".join(entrada.split()).title())
        print("Carro adicionado!")

        confirmacao = input("Quer adicionar mais?(s ou n) ").lower()

    if confirmacao == 'n':
        return

    else:
        ("s ou n cavalo")

def RemoveList(cars, motos):
    escolha = input("de 'C' carro ou 'M' moto? ").upper()

    if escolha == 'C':
        remocao = input("Digite o nome do carro que deseja remover: ").title().strip()
        if remocao in cars:
            cars.remove(remocao)
            print(f"Carro {remocao} removido!")
        else:
            print(f"Esse tal de {remocao} não foi encontrado na lista.")


    elif escolha == 'M':
        remocao = input("Digite o nome da moto que deseja remover: ").title().strip()
        if remocao in motos:
            motos.remove(remocao)
            print(f"Sua {remocao} foi removida!")
        else:
            print(f" {remocao} não encontrada na lista.")


    else:
        print("Escolha inválida.")

motos = []

cars = []

while True:
    print("Benvenido a su lista de deserros")
    opcao = int(input("Escolha uma opção:\n1.Add moto\n2.Add carro\n3.listar motos\n4.listar carros\n5.excluir algum\n"))
    if opcao == 1:
        AddMotors()
    
    elif opcao == 2:
        AddCar()

    elif opcao == 3:
        if not motos:
            print("Você não tem motos na lista.")
        else:
            motosFormated = ", ".join(motos).title()
            print(f"Motos que você já tem: {motosFormated}")

    elif opcao == 4:
        if not cars:
            print("Você não tem carros na lista.")
        else:
            carsFormated = ", ".join(cars).title()
            print(f"Carros que você já tem: {carsFormated}")

    elif opcao == 5:
        RemoveList(cars, motos)

    else:
        print("Escolhe oq pode")

#Functions used and motivations for this:

#split| para dividir uma lista em uma lista de substrings
#title| para deixar a primeira letra de cada palavra maiúscula(só consegui usar por causa do split)
#strip| para remover espaços no começo e no fim da string
#join| para unir os elementos com um separador personalizado, tirando: '',[] das listas
#upper| para deixar tudo em maiúsculo nas entradas para evitar erro
#lower| para deixar tudo em minúsculo nas entradas para evitar erro