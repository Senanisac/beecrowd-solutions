
# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

linha1 = input().split()
diai = int(linha1[1])

linha2 = input().split()
hhi = int(linha2[0])
mmi = int(linha2[2])
ssi = int(linha2[4])

#Conversoa en segundos
totali = (86400 * diai) + (3600 * hhi) + (60 * mmi) + ssi 


linha3 = input().split()
diaf = int(linha3[1])

linha4 = input().split()
hhf = int(linha4[0])
mmf = int(linha4[2])
ssf = int(linha4[4])

#Conversoa en segundos
totalf = (86400 * diaf) + (3600 * hhf) + (60 * mmf) + ssf

diff = totalf - totali

dias = diff // 86400 #retornar somente a parte inteira
diff = diff % 86400  #retornar somente o resto

horas = diff // 3600
diff = diff % 3600

minutos = diff // 60
segundos = diff % 60

print(f"{dias} dia(s)")
print(f"{horas} hora(s)")
print(f"{minutos} minuto(s)")
print(f"{segundos} segundo(s)")

