notasAlunos = [
      ["Fábio", [10, 9], [10, 8]],
      ["Aline", [7, 7], [10, 7]],  
      ["Maria", [6, 2], [8, 2]] 
]

for i in range(len(notasAlunos)):
    print(f"posição {i} - Nome: {notasAlunos[i][0]} médiaB1: { (notasAlunos[i][1][0] + notasAlunos[i][1][1]) / 2}")