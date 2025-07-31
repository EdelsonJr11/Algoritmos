nota = input("Digite sua nota das provas e da prova final: ")

b1, b2, pf = map(float, nota.split()) #split é "Separar", ele pega os valores separados por espaço e retorna uma lista
# o MAP mapeia e faz estas alteraçôes
mediaB = (b1 + b2) / 2

if mediaB >= 7:
    print("Aprovado por média")
elif mediaB < 7 and pf >= 6:
    print("Aprovado por prova final")
else:
    print("reprovado!")