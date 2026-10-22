
numero = int(input())
cara = input()

matriz = []

#Construcao da matriz
for i in range(12):
    linha = []
    for j in range(12):
        valor = float(input())
        linha.append(valor)
    matriz.append(linha)

linha = matriz[numero]
soma = sum(linha)

if cara == "S":
    print(f"{soma:.1f}")
elif cara == "M":
    media = soma / 12
    print(f"{media:.1f}")

