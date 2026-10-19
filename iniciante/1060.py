
contador = 0
i = 0
while i < 6:
    valor = float(input())  
    if valor > 0:
        contador = contador + 1
    i += 1

print(f"{contador} valores positivos")