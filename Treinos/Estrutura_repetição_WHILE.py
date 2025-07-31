while True:
    moto = int(input("Digite a moto que você quer:\n 1.Bandit\n 2.Ninja \n 3. Cb 300 \n '0' para encerrar): "))
    if moto == 0:
        print("Encerrando o programa...")
        break
    elif moto == 1:
        print("Você não tem dinheiro, se aquieta!")
    elif moto == 2:
        print("Boa escolha!")
    elif moto == 3:
        print("OLHA O CABEÇOTEEE")
    else:
        print("Você não sabe o que quer, né? Escolha uma moto válida ou digite '0' para encerrar.")