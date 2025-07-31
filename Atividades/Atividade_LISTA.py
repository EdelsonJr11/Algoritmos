def calcularPeso(peso):
    imc = peso / (altura**2)
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal, parabéns!"
    elif imc < 30:
        return "Sobrepeso em"
    elif imc < 35:
        return "Obesidade grau I(pesadinho né fi)"
    elif imc < 40:
        return "Obesidade grau II (graúdo em pai)"
    else:
        return "Obesidade grau III (Vai morrer infiliz)"
    
def calcularIdade(ano_de_nascimento):
    resultado = 2025 - ano_de_nascimento
    return resultado

def escolhas():
    confirmacao = input("Deseja realizar o seu cadastro? (s/n) \nJÁ TEM? 'c' para consultar\n").lower()
    
    if confirmacao == "s":
        print("Okey de boa!")

    elif confirmacao == "n":
        print("Cadastro cancelado.")
        exit()

    elif confirmacao == "c":
        consultarDados()
    
    else:
        print("é s ou n ou c papai vem com essa não para de moda")
        exit()

def adicionarNaLista():
    pessoa = [nome, apelido, idade, peso, altura]
    dados.append(pessoa)

def consultarDados():
    if dados == []:
        print("Nem tem macho, cadastra primeiro")
        escolhas()
    
    for i, pessoa in enumerate(dados):
        print(f"\npessoa {i+1}")
        print(f"-Nome: {pessoa[0]}\n-Vulgo: {pessoa[1]}\n-Idade: {pessoa[2]}\n-Peso: {pessoa[3]}, inclusive, {calcularPeso(peso)}\n-Altura:{pessoa[4]}")
    escolhas()
    
dados = []
while True:
    escolhas()

    nome = input("Digite o nome da pessoa: ")
    apelido = input("Digite o apelido: ")
    ano_de_nascimento = int(input("Digote seu ano de nascimento: "))

    idade = calcularIdade(ano_de_nascimento)

    peso = float(input("Digote seu peso(em kg): "))
    altura = float(input("Digite sua altura(com ponto): "))

    adicionarNaLista()

    print("Dados cadastrados!")



