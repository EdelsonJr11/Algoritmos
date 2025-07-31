def adicionar_materia(materias):
    materia = input("Digite o nome da matéria: ")
    dia_da_semana = input("Digite o dia da semana que vai estudá-la (ex: Seg, Ter, Qua): ")
    horario = input("Digite o horário de estudo (ex: 14:00 - 16:00): ")
    materias[materia] = (dia_da_semana, horario)
    print(f"Matéria {materia} na(o) {dia_da_semana} adicionada com sucesso!")

def listar_materias(materias):
    if not materias:
        print("Cadastre uma ou mais matérias primeiro!")

    for materia in materias:
        print("-",materia)

def mostrar_horario(materias):
    if not materias:
        print("Cadastre uma ou mais matérias primeiro!")

    for (materia, (dia_da_semana, horario)) in materias.items():
        print(f"{materia} | {dia_da_semana}: {horario}")

def remover_materia(materias):
    if not materias:
        print("Tá querendo tirar oq nem tem?")
        return

    remocao = input("Qual quer tirar?")
    if remocao in materias:
        confirmacao = input(f"Tem certeza que quer remover {remocao}? (s/n): ").upper()
    
        if confirmacao == 'N':
            print(f"{remocao} não foi removida.")
            return
        elif confirmacao == 'S':
            del materias[remocao]
            print(f"{remocao} Removida com sucesso!")
        else:
            print("é só 's' ou 'n', espertão.")

    else:
        print(f"{remocao} não está na lista de matérias. Veja se digitou certo ou se já foi removida.")

materias = {}#Criando o dicionário fora de tudo para que ele não seja reiniciado a cada iteração do loop

while True:
    print("Edelsing organization de estudos")
    opcao = int(input("Escolha uma opção:\n1. Adicionar matéria\n2. Listar matérias\n3. Mostrar meu horário\n4. Remover matéria\n5. Sair\nOpção: "))

    if opcao == 5:
        print("Saindo do organizador de estudos. Até mais!")
        break
    elif opcao == 1:
        adicionar_materia(materias)
    elif opcao == 2:
        listar_materias(materias)
    elif opcao == 3:
        mostrar_horario(materias)
    elif opcao == 4:
        remover_materia(materias)
        