telefone = '8999445-1988'
print(telefone[0])
print(telefone[5])
print(telefone[11])

#Método find() ENCONTRAR procura a primeira vez que aparece e retorna o índice do início da ocorrência

if(telefone.find('89') == -1):
    print("Outro DDD")

else:
    print("DDD 89")

#Função strip() retira os espaços no começo ou no fim de uma STR

nome = '  Edelson Júnio'
nome2 = 'Edelson Júnior'
nome3 = 'EdelsonJúnior  '
nome4 = ' Edelson Júnior '
print(nome.strip(), nome2.strip(), nome3.strip(), nome4.strip())

#replace() vai sobrescrever oq eu mandar por oq eu mandar

n = '(89)99445-1988'
n = n.replace( '(', '')
print(n.replace( ')', ''))

#o split() vai desmenbrar uma string ou lista em substrings e retornar os valores em um array

n = 'Edelson Antônio de Sousa Júnior'
nAlterado = n.split()
print(n)
print(nAlterado)

sobrenome = nAlterado[1]
print(sobrenome)