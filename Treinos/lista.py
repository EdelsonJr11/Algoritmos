#é o mesmo que vetor array ou lista.
#o array não é tipado.
array = [1,2,3,4,5]

#aqui eu estou mudando o valor do segundo elemento do array
array[1] = 10 

#.append ADICIONA UM ELEMENTO AO FINAL DO ARRAY
array.append(6)
array.append("Edelson")
array.append(1.35)

# .pop REMOVE UM ELEMENTO DO ARRAY
array.pop(0)

#aqui eu estou imprimindo o array completo
print(array)

#aqui eu estou imprimindo o segundo elemento do array
print(array[1])

#aqui eu estou imprimindo os 3 primeiros elementos do array
print(array[0:3])

#Array com for

for i in array:
    print(i)


