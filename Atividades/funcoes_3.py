def trianguloValido():
    lados = input("Digite os 3 lados do triângulo(separados por espaço):")
    lado_a, lado_b, lado_c = map(int, lados.split())

    if lado_a + lado_b <= lado_c or lado_a + lado_c <= lado_b or lado_b + lado_c <= lado_a:
        print("Digite um triângulo válido!")
        
    elif   lado_a == lado_b == lado_c:
     print("Isso não só é um triângulo, como é um triângulo equilátero")
     
    elif lado_a != lado_b and lado_a != lado_c and lado_c != lado_b:
     print("isso é um triângulo do tipo escaleno!!")

    else: print("isso é um triangulo isórceles.")

def areaDoTereno():
    tamanho = float(input("Digite o tamanho do terreno em metros quadrados: "))
    largura = float(input("Digite a largura do terreno: "))
    area = tamanho * largura
    print(f"A área do terreno é de {area} metros quadrados.")

def areaDaCrircunferencia():
    pi = 3.14
    raio = float(input("Digite o raio da circunferência: "))
    area = 2 * pi * raio * raio
    print(f"a area da circunceferência é {area}")

while True:
    print(" 1. Verificar Tipo de Triângulo \n 2. Verificar Área do Terreno \n 3. Verificar Área da Circunferência\n 4. Sair")
    opcao = int(input("Digite o número da opção desejada: "))
    if opcao == 4:
        break
    elif opcao == 1:
       trianguloValido()
    elif opcao == 2:
        areaDoTereno() 
    elif opcao == 3:
        areaDaCrircunferencia()

    