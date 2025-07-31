geral = []
def adicionarAluno():
    nome = (input("Digite o nome do aluno: "))

    nota_b1 = []
    nota_b1.append(float(input("Digite a 1ª nota do primeiro bimestre: ")))
    nota_b1.append(float(input("Digite a 2ª nota do primeiro bimestre: ")))

    nota_b2 = []
    nota_b2.append(float(input("Digite a 1ª nota do segundo bimestre: ")))
    nota_b2.append(float(input("Digite a 2ª nota do segundo bimestre: ")))

    alunos = [nome, nota_b1, nota_b2]
    geral.append(alunos)

    print("Aluno adicionado com sucesso!")

def calcularMediaGeral():
    for i in range (len(geral)):
        mediaGeral = ((geral[i][1][0] + geral[i][1][1]) / 2) + ((geral[i][2][0] + geral[i][2][1]) / 2) /2
        return mediaGeral

def calcularMediaBimestral():
    for i in range (len(geral)):
        mediaB1 = (geral[i][1][0] + geral[i][1][1]) / 2
        mediaB2 = (geral[i][2][0] + geral[i][2][1]) / 2
        print(f"Aluno:{i+1} - Nome: {geral[i][0]} \n - Média_B1: {mediaB1} \n - Média_B2: {mediaB2} \n - Média Geral: {calcularMediaGeral()}")



while True:
    print("Bem-vindo ao sistema de notas desgraça! Escolha uma opção:")
    escolha = int(input("1.adicionar aluno\n2.listar boletins\n3.Médias bimestrais dos alunos\n 4.situação dos alunos\n 5.sair:\n"))
    if escolha == 5:
        print("Saindo do sistema de notas. Até mais!")
        break
    elif escolha == 1:
        adicionarAluno()
    elif escolha == 2:
        print(f"Boletins dos alunos:{geral}")
    elif escolha == 3:
        calcularMediaBimestral()
    elif escolha == 4:
        nome = input("Digite o nome do aluno para verificar a situação: ")
    else:
        print("Opção inválida. Tente novamente.")




 
