
#Ler tres valores 
A, B, C = input().split()

#Converter para os tipos apropriados
A = float(A)
B = float(B)
C = float(C)

#Area do triangulo
tri = (A * C) / 2
print(f"TRIANGULO: {tri:.3f}")

#Area do circulo
cir = 3.14159 * C**2
print(f"CIRCULO: {cir:.3f}")

#Area do trapezio
tra = ((A + B) * C) / 2
print(f"TRAPEZIO: {tra:.3f}")

#Area de quadrado 
qua = B**2
print(f"QUADRADO: {qua:.3f}")

#Area do retangulo
ret = A * B
print(f"RETANGULO: {ret:.3f}")

