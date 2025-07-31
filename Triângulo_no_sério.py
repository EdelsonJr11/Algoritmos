angulos = input("Digite os 3 ângulos do triângulo(separados por espaço):")

an_1, an_2, an_3 = map(int, angulos.split())

lados = input("Digite os 3 lados do triângulo(separados por espaço):")

lado_a, lado_b,lado_c = map(int, lados.split())

if an_1 + an_2 + an_3 != 180 :
    print("Isso nem é um triÂngulo, jumento(por causa dos ângulos; tem q da 180)")
else:
     if lado_a == lado_b == lado_c:
          print("Isso não só é um triângulo, como é um triângulo equilátero")
     else: 
         if lado_a != lado_b and lado_a != lado_c and lado_c != lado_b:
              print("isso é um triângulo do tipo escaleno!!")

         else: print("isso é um triangulão isorcelão")