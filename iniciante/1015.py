
#Ler x e y do ponto 1
x1, y1 = map(float, input().split())

#Ler xe y do ponto 2
x2, y2 = map(float, input().split())

#Calcular a distancia entre os dois pontos
u = (x2 - x1)**2
v = (y2 - y1)**2
dist = (u + v)**0.5

#Imprimir a distancia
print(f"{dist:.4f}")

