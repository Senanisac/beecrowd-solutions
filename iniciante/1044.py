
#Leitura dos valores e conversao
a, b = map(int, input().split())

#Condicoes e saidas
if ((a % b) == 0) or ((b % a) == 0):
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")

