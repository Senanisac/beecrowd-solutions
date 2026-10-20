
contador = 0
soma = 0
for i in range(6):
    valor = float(input())
    if valor > 0:
        contador = contador + 1
        soma = soma + valor
 
media = soma / contador #deve ter pelos menos um numero positivo
print(f"{contador} valores positivos")
print(f"{media:.1f}")