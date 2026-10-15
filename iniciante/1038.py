
#Ler dois valores e converter em inteiro
codigo, qtd = map(int, input().split())

#condicoes e saida
if codigo == 1:
    valor = qtd * 4.00
    print(f"Total: R$ {valor:.2f}")
elif codigo == 2:
    valor = qtd * 4.50
    print(f"Total: R$ {valor:.2f}")
elif codigo == 3:
    valor = qtd * 5.00
    print(f"Total: R$ {valor:.2f}")
elif codigo == 4:
    valor = qtd * 2.00
    print(f"Total: R$ {valor:.2f}")
else:
    valor = qtd * 1.50
    print(f"Total: R$ {valor:.2f}")

