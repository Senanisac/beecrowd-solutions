
a = []

for i in range(100):
    valor = float(input())
    a.append(valor)

for posicao, ele in enumerate(a):
    if ele <= 10.0:
        print(f"A[{posicao}] = {ele:.1f}")

