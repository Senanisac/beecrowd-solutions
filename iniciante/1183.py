
cara = input()

matriz = []

#Construcao do matriz 
for i in range(12):
    linha = []
    for j in range(12):
        valor = float(input())
        linha.append(valor)
    matriz.append(linha)
    
#Construcao do diagonal
diagonal = []
for i in range(12):
    for j in range(12):
        if j > i:
            diagonal.append(matriz[i][j])

soma = sum(diagonal)

if cara == "S":
    print(f"{soma:.1f}")
elif cara == "M":
    media = soma / 66
    print(f"{media:.1f}")

