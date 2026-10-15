
import math

#Ler os tres valores e converter em pontos flutuantes 
a, b, c = map(float, input().split())


#Calcular delta 
delta = b**2 - (4*a*c)


#Condicoes e saida
if a == 0:
    print("Impossivel calcular")
elif delta < 0:
    print("Impossivel calcular")
else:
    deltaf = math.sqrt(delta)
    r1 = (-b + deltaf) / (2*a)
    r2 = (-b - deltaf) / (2*a)
    print(f"R1 = {r1:.5f}")
    print(f"R2 = {r2:.5f}")
    
