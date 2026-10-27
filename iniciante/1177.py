
t = int(input())
valor = 0

for i in range(1000):
    if valor < t:
        print(f"N[{i}] = {valor}")
        valor = valor + 1
    else:
        valor = 0
        print(f"N[{i}] = {valor}")
        valor = valor + 1
        

