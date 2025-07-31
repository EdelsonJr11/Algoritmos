import re
def cadastroValid(dados):
    nome = input("Digote seu nome ")
    sobrenome = input("Digite seu sobrenome ")
    endereco = input("Digite seu endereço ")
    cep = input("Digite seu CEP ")
    tel = input("Digite seu telefone ")
    email = input("Digite seu email ")

    all = [nome, sobrenome, endereco, cep, tel, email]

    dados.append(all)

    print("Cadastrou!")
#validação
    padrao = '([0-9]{2,3})?(\([0-9]{2}\))([0-9]{4,5})([0-9]{4})'
    if re.match(padrao, tel):




def listar(dados):
        for i in range(len(dados)):
            nome = dados[i][0]
            sobrenome = dados[i][1]
            endereco = dados[i][2]
            cep = dados[i][3]
            tel = dados[i][4]
            email = dados[i][5]
            print(f" -Nome:{nome} {sobrenome} \n -Endereço: {endereco} \n -CEP: {cep} \n -Telefone: {tel} \n -Email: {email}")  


  
dados = []
while True:
    print("Bem-Vindo ao cadastramente exaustivo de usuários com o objetivo de que eu aprenda")

    opcao = int(input("\nEscolha:\n1.Cadastrar usuário\n2.Listar usuários \n"))

    if opcao == 1:
        cadastroValid(dados)

    elif opcao == 2:
         listar(dados)