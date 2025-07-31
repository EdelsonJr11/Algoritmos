#TRIDIMENCIONAL
kawasaki_ninja = [
    ["cilindrada", [250, 300], [600, 636]], # tem a dimensão de tudo(terceira dimensão, vem na vertical o coxete rosa).
    ["cavalos", [33, 40], [80, 102]],       # a dos elementos da linha(contando a string)(segunda dimensão).
    ["ano", [2008, 2013], [2012, 2016]]     # os elementos que tem dentro dos arrays(os números) que estão na segunda(terceira dimensão).
]
print(kawasaki_ninja)

#acessar elementos dele
#quero o 80. tenho que percorrer por as dimensões 
print(kawasaki_ninja[1][2][0])

print(kawasaki_ninja[1][1][0])#33
print(kawasaki_ninja[0][1][1])#300
print(kawasaki_ninja[2][1][0])#2008