lista = []
while True:
    print("Adicione pessoas a lista")
    confirmacao = input("Quer adicionar mesmo (s/n)?").lower()
    nome = input("Digite o nome da pessoa: ")
    apelido = input("Digite o apelido: ")
    idade = int(input("Digote a idade: "))
    peso = float(input("Digote seu peso: "))
    
    
    if confirmacao == "s":
        lista.append(nome)
        lista.append(apelido)
        lista.append(idade)
        lista.append(peso)
        print(f"Esse tal de {lista[0]} vulgo {lista[1]} e tem {lista[2]} anos e pesa {lista[3]}kg")

    elif confirmacao == "n":
        break
        

