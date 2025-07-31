#Usa uma chave relacionada com valores

#dict cria o dicionário
#update adiciona valores e chaves no dicionário
infos = dict(nome = "Edelson", idade = 18, curso = "ADS", estadoBoniteza = "perfeito")
print(infos)

infos.update(altura = 1.68)
print(infos)

#para alterar valores usa o update com a mesma chave
infos.update(nome = "Adinelson")
print(infos)

#get pega o valor da chave que eu quiser
print(infos.get("nome"))

#Criando um dicionário comopleto
moto = {
    "Marca": "Kawasaki",
    "Modelo": "Ninja",
    "Cilindrada": "249",
    "Cavalaria": "33",
    "torque": "2,3"
}
print(moto)

#Criando a partir de um dicionário vazio
moto2 = {}

moto2["Marca"] = "Kawasaki"
moto2["Modelo"] = "Ninja"
moto2["Cilindrada"] = "249"
moto2["Cavalaria"] = 33
moto2["Torque"] = 2.3

print(moto2)

#pop remove
moto2.pop("Marca")
moto2.pop("Modelo")
print(moto2)

#Usando o FOR com Dicionário
for i in infos:
    valor = infos[i]
    print(valor)