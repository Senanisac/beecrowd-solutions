
#Leitura dos valores e conversoa 
a, b, c = map(float, input().split())

#Verificacao e condicoes

if ((a + b) > c) and ((b + c) > a) and ((c + a) > b):
    per = a + b + c
    print(f"Perimetro = {per:.1f}")
else:
    are = (a + b) * c
    area = are / 2
    print(f"Area = {area:.1f}")
    
