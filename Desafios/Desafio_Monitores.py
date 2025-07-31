import math
while True:
    print("ESCOLHA UMA OPÇÃO:")
    opcoes = input("1-Calcular arranjo(ordem importa)\n2-Calcular combinação(ordem não imprta)\n3-Sair\n")
    if opcoes == "3":
        print("Saindo do programa...")
        break
    elif opcoes == "1":
        n = int(input("Digite o valor de n(Quantos números quer posicionar): "))
        p = int(input("Digite o valor de p(Quantas posições quer ocupar): "))
        if p > n:
            print("O valor de p não pode ser maior que n. Tente novamente.")
            continue

        arranjo = math.factorial(n) / math.factorial(n-p)

        print(f"Você pode organizar {n} números em {p} posições de {arranjo} formas, sem poder repeti-las.")

    elif opcoes == "2":
        n = int(input("Digite o valor de n(Quantos números vão se organizar):"))
        p = int(input("Digite o valor de p(Quantas posições vão se ocupar): "))
        if p > n:
            print("O valor de p não pode ser maior que n. Tente novamente.")
            continue

        combinacao = math.factorial(n) / ( math.factorial(p) * math.factorial(n-p) )

        print(f"Você pode organizar {n} números em {p} posições de {combinacao} formas, podendo repeti-las.")

    else:
        print("Opção inválida, tente novamente.")
        continue