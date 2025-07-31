import re

name = "Edelson Antonio de Júnior"

#search procura se tem expressões regulares

nameAltered = re.search("Edelson", name)

print(nameAltered)

nameAltered2 = re.search("^Edelson.*Antonio$" ,name)
print(nameAltered2)

#o match valida um tipo de dados

telefone = '5589994451988'
padrao = '( [0-9] {2,3}) ? (\([0-9] {2} \)) ([0-9] {4,5}) ([0-9]{4})'
if re.match(padrao, telefone):
    print("válido")
else:
    print("INVÁLIDO")