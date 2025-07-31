while True:
    estado = (input("Digite o estado que você quer saber a capital:\n PI - Piauí\n RJ - Rio de Janeiro \n MG - Minas Gerais \n RR - Rorraima \n 's' para encerrar): ")).upper()
    if estado == 'S':
        print("Até mais, Pedro Alvares Cabral!")
        break
    elif estado == "PI":
        print("A capital do Piauí é Teresina.")
    elif estado == "RJ":
        print("A capital do Rio de Janeiro é Rio de Janeiro.")
    elif estado == "MG":
        print("A capital de Minas Gerais é Belo Horizonte.")
    elif estado == "RR":
        print("A capital de Roraima é Boa Vista.")
    else:
        print("Valeu, Pedro Alvares Cabral! esolhe um que tem ou 's' para encerrar.")