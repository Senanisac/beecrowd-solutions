
#Ler os tres valores e converter em inteiro com map
a, b, c = map(int, input().split())

#Calcular o maior entre a e b
maiorab = (a + b + abs(a-b)) / 2
maiorab = int(maiorab)

#Calcular maior entre maiorab e c
maiorf = (maiorab + c + abs(maiorab-c)) / 2
maiorf = int(maiorf)

#Imprimir maiorf
print(f"{maiorf} eh o maior")

