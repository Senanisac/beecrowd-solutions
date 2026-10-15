
#Ler o valor 
valor = float(input())


#Condicoes e saida
if valor < 0 or valor > 100:
    print("Fora de intervalo")
elif valor > 75 and valor <= 100:
    print("Intervalo (75,100]")
elif valor > 50 and valor <= 75:
    print("Intervalo (50,75]")
elif valor > 25 and valor <= 50:
    print("Intervalo (25,50]")
else:
    print("Intervalo [0,25]")

