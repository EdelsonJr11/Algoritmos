
##### TRIDIMENCIONAL MANUAL #######
Edelson = []
Edelson.append("Edelson")

Edelson2 = []
Edelson2.append(10)
Edelson2.append(11.5)

Edelson.append(Edelson2)

Edelson3 = []
Edelson3.append(11)
Edelson3.append(10.5)

Edelson.append(Edelson3)

############################

Pedro = []
Pedro.append("Pedro")

Pedro2 = []
Pedro2.append(1)
Pedro2.append(2)

Pedro.append(Pedro2)

Pedro3 = []
Pedro3.append(7)
Pedro3.append(4)

Pedro.append(Pedro3)

###########################

AP = []
AP.append("Antônio Pedro")

AP2 = []
AP2.append(4)
AP2.append(1)

AP.append(AP2)

AP3 = []
AP3.append(7)
AP3.append(5)

AP.append(AP3)

##########################

tudo = []
tudo.append(Edelson)
tudo.append(Pedro)
tudo.append(AP)

for i in range (len(tudo)):
    for j in range (len(tudo[i])):
        print(tudo[i][j])