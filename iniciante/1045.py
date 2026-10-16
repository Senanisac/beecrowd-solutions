
#Leitura dos tres valores e conversao
A, B, C = map(float, input().split())

#Construir uma lista, ordenar e faazer as attribucoes
lista = sorted([A, B, C], reverse=True)
a, b, c = lista[0], lista[1], lista[2]

#Condicoes e saidas
if a >= (b + c):
    print("NAO FORMA TRIANGULO")
else:
    if a**2 == (b**2 + c**2):
        print("TRIANGULO RETANGULO")
    elif a**2 > (b**2 + c**2):
        print("TRIANGULO OBTUSANGULO")
    elif a**2 < (b**2 + c**2):
        print("TRIANGULO ACUTANGULO")
    
    if a == b == c:
        print("TRIANGULO EQUILATERO")
    elif a == b or b == c or c == a:
        print("TRIANGULO ISOSCELES")

