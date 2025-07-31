angulos = input("Digite os 3 ângulos do triângulo(separados por espaço):")

an_1, an_2, an_3 = map(int, angulos.split())

if an_1 + an_2 + an_3 != 180 :
    print("Isso nem é um triÂngulo, incompetente!(por causa dos ângulos; tem que dar 180)")
    exit()

lados = input("Digite os 3 lados do triângulo(separados por espaço):")

lado_a, lado_b,lado_c = map(int, lados.split())

if   lado_a == lado_b == lado_c:
     print("Isso não só é um triângulo, como é um triângulo equilátero")
     
elif lado_a != lado_b and lado_a != lado_c and lado_c != lado_b:
     print("isso é um triângulo do tipo escaleno!!")

else: print("isso é um triangulo isórceles.")