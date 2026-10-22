
c = int(input())
t = input()

matriz = []

#Construcoa do matriz
for i in range(12):
    linha = []
    for j in range(12):
        valor = float(input())
        linha.append(valor)
    matriz.append(linha)

#Recuparar os valores de uma coluna
coluna = []
for i in range(12):
    valor = matriz[i][c]
    coluna.append(valor)

soma = sum(coluna)

if t == "S":
    print(f"{soma:.1f}")
elif t == "M":
    media = soma / 12
    print(f"{media:.1f}")

