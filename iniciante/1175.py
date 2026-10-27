
n = []

for i in range(20):
    valor = int(input())
    n.append(valor)
    

n = reversed(n)

for posicao, ele in enumerate(n):
    print(f"N[{posicao}] = {ele}")

