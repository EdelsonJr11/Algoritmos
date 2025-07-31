while True:
    print("Aqui você faz sua 'Noite Estrelada!'")
    quantColunas = int(input("Quantas estrelas você quer no seu céu?\n"))
    quantLinhas = int(input("Quantas camadas você quer no seu céu?\n"))
    simboloColunas = input("Qual símbolo você quer usar para as estrelas?\n ")

    if quantColunas <= 0 or quantLinhas <= 0:
        print("Coloca estrela nesse céu, rapaiz!")
        continue
    else:
            for _ in range(quantLinhas):
                    print(quantColunas * simboloColunas)
            