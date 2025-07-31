while True:
    opcao = int(input("Escolha uma opção: \n 1.Calculadora \n 2.tabuada \n 3.Sair\n"))
    if opcao == 3:
        break
    elif opcao == 1:
        n1 = int(input("Digite um número: "))
        operacao = input("Digite a operação desejada (+, -, *, /): ")
        n2 = int(input("Digite o outro número: "))
        if operacao == "+":
                print(f"{n1} + {n2} = {n1 + n2}")
        elif operacao == "-":
            print(f"{n1} - {n2} = {n1 - n2}")
        elif operacao == "*":
            print(f"{n1} * {n2} = {n1 * n2}")
        elif operacao == "/":
            if n2 != 0:
                print(f"{n1} / {n2} = {n1 / n2}")
            else:
                print("Erro: Divisão por zero não é permitida.")
        else:
            print("escolhe um que tem.")

    elif opcao == 2:
        n = int(input("Digite um número para ver a tabuada: "))
        for i in range(1, 11):
            print(f"{n} x {i} = {n * i}")
    else:
        print("pode n man")
        