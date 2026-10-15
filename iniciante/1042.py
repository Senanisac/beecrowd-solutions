
#Leitura dos valores e conversao
a, b, c = map(int, input().split())

#Criar uma lista com os valores
ori = [a, b, c]

#Ordenar os valores em forma crescente
tries = sorted(ori)

#Imprimir os valores
print(tries[0])
print(tries[1])
print(tries[2])

print()

#Imprimir a lista original
print(ori[0])
print(ori[1])
print(ori[2])

