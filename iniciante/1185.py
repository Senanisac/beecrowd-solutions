
caractere = input()

#Construcao do matriz
matriz = []

for i in range(12):
    linha = []
    for j in range(12):
        valor = float(input())
        linha.append(valor)
    matriz.append(linha)
    
#Recuperao dos dados abaixa da diogonal
acima = []

for i in range(12):
    for j in range(12):
        if i+j < 11:
            acima.append(matriz[i][j])
    
soma = 0.0
for valor in acima:
    soma = soma + valor
    
if caractere == "S":
    print(f"{soma:.1f}")
elif caractere == "M":
    media = soma / 66

