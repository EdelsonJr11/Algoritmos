import random

turmas = {}
infoAlunos = {}

def cadastroTurma():
    print("Cadastro de turmas!!!!!")
    codigoTurma = random.randint(1, 99)
    moduloTurma = int(input("Digite o número do módulo/período que a turma está: "))
    nivelEnsinoTurma = input("Nível de ensino da turma. (Superior, médio e etc...) ").title()

    turmas[codigoTurma] = {
        "moduloTurma": moduloTurma,
        "nivelEnsinoTurma":nivelEnsinoTurma,
        'matriculaAlunos': {}
    }

    print(f"Sua turma nível: {turmas[codigoTurma]['nivelEnsinoTurma']} do período {turmas[codigoTurma]['moduloTurma']} foi cadastrada! Código da turma: {codigoTurma}")


def listarTurmas():
    for codigoTurma in turmas:
        print(f"- Turma: {codigoTurma}|Nível: {turmas[codigoTurma]['nivelEnsinoTurma']}| Módulo: {turmas[codigoTurma]['moduloTurma']}")


def listarAlunos():
    for matriculaAluno in infoAlunos:
        print(f"- aluno: {infoAlunos[matriculaAluno]['nomeAluno']}| de {infoAlunos[matriculaAluno]['idadeAluno']} anos| Turma: {infoAlunos[matriculaAluno]['turmaCodigo']}| Matrícula: {matriculaAluno}")


def cadastrarAluno():
    print("Cadastre seu aluno!!")
    nomeAluno = input("Digite o nome do aluno: ").title()
    idadeAluno = int(input("Digite a idade do aluno: "))

    matriculaAluno = random.randint(0, 99)
    sigla = input("Sigla do nivel de ensino do aluno: ").upper()
    turmaCodigo = int(input("Digite o código da turma que o aluno vai: "))
    
    if turmaCodigo in turmas:
        print("turma encontrada!")
    else:
        print("turma não encontrada, tente de novo.")
        return cadastrarAluno()
    
    matriculaAluno = sigla + str(turmaCodigo) + str(matriculaAluno)

    print("Esta é a matrícula dele! ", matriculaAluno)

    infoAlunos[matriculaAluno] = {
        'nomeAluno' : nomeAluno,
        'idadeAluno' : idadeAluno,
        'turmaCodigo' : turmaCodigo,
        'matricula' : matriculaAluno
     }
        
    if turmaCodigo in turmas:
        turmas[turmaCodigo]['matriculaAlunos'][matriculaAluno] = infoAlunos[matriculaAluno]['matricula']
        print(f"{nomeAluno} foi cadastrado na turma {turmaCodigo} com a matrícula {matriculaAluno}.")

    elif turmaCodigo not in turmas:
        print("Turma não encontrada. Tente novamente.")


def edicao():
    def editarTurma():
        while True:
            print(f"Essas são as turmas cadastradas: ")
            listarTurmas()
            escolha = int(input("Escolha o que quer editar: \n1.Modulo\n2.Nivel de ensino\n3.Excluir turma\n4.Sair\n"))

            if escolha == 1:
                codigoTurma = int(input("Digite o código da que queres editar: "))
                if codigoTurma in turmas:
                    turmas[codigoTurma]['moduloTurma'] = int(input("Novo módulo"))
                    print("Editado!!")

            if escolha == 2:
                codigoTurma = int(input("Digite o código da que queres editar: "))
                if codigoTurma in turmas:
                    turmas[codigoTurma]['nivelEnsinoTurma'] = input("Novo Nível de ensino").title()
                    print("Editado!!")

            if escolha == 3:
                codigoTurma = int(input("Digite o código da que queres deletar: "))
                if codigoTurma in turmas:
                    del turmas[codigoTurma]
                    print("turma excluída!")
            if escolha == 4:
                break

            else:
                print("Opção inválida!!")


    def editarAluno():
        while True:
            print(f"Esses são os alunos cadastrados:")
            listarAlunos()
            escolha = int(input("Escolha o que quer editar: \n1.Nome\n2.idade\n3.Excluir aluno\n4.Sair\n"))

            if escolha == 1:
                matricula = input("Digite a matrícula do que queres editar: ").upper()
                if matricula in infoAlunos:
                    infoAlunos[matricula]['nomeAluno'] = input("Novo nome").title()
                    print("Editado!!")

            if escolha == 2:
                matricula = input("Digite a matrícula do que queres editar: ").upper()
                if matricula in infoAlunos:
                    infoAlunos[matricula]['idadeAluno'] = int(input("Nova idade"))
                    print("Editado!!")

            if escolha == 3:
                matricula = input("Digite a matrícula do que queres deletar: ").upper()
                if matricula in infoAlunos:
                    del infoAlunos[matricula]
                    print("aluno excluído!")

            if escolha == 4:
                break

            else:
                print("Opção inválida!")


    while True:
        opcao = int(input("quer editar oq: \n1.Editar turma\n2.Editar aluno\n3.Sair\n"))
        if opcao == 1:
            editarTurma()
        elif opcao == 2:
            editarAluno()
        elif opcao == 3:
            break


while True:
    print("__SUAP Edelson__")
    escolha = int(input("Escolha uma das opções principais: \n1.Cadastrar nova turma\n2.Listar turmas do sistema\n3.Cadastrar aluno\n4.listar alunos\n5.Editar\n6.Sair\n"))

    if escolha == 1:
        cadastroTurma()

    elif escolha == 2:
        listarTurmas()

    elif escolha == 3:
        cadastrarAluno()
    
    elif escolha == 4:
        listarAlunos()

    elif escolha == 5:
        edicao()

    elif escolha == 6:
        break

    else:
        print("escolhe oq tem.")