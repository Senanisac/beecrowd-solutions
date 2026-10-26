
def eh_negativo_nulo(numero, i):
    if numero > 0:
        print(f"X[{i}] = {numero}")
    else:
        print(f"X[{i}] = 1")


for i in range(10):
    valor = int(input())
    eh_negativo_nulo(valor, i)

