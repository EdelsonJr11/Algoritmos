while True:
    print("Este é um program inútil para você saber se seu ddd é do Piauí.")

    telNumber = str(input("Telefone ou 0 pra sair: "))

    if telNumber == '0':
        break

    if telNumber.find('89') == 0 or telNumber.find('86') == 0:
        print("Seu ddd é do Piauí.")
        continue
    else:
        print("Seu ddd não é do Piauí.")
