
caractere = input()

matriz = []

for i in range(12):
    linha= []
    for j in range(12):
        valor = float(input())
        linha.append(valor)
    matriz.append(linha)
    
areadir = []

for i in range(12):
    for j in range(12):
        if (j > i) and (i+j > 11):
            areadir.append(matriz[i][j])
            
            
soma = sum(areadir)

if caractere == "S":
    print(f"{soma:.1f}")
elif caractere == "M":
    media = soma / 30
    print(f"{media:.1f}")

