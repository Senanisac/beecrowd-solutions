
valor = float(input())
centavos = round(valor * 100)  # converter en centavos

print("NOTAS:")
nota100 = centavos // 10000
centavos %= 10000
print(f"{nota100} nota(s) de R$ 100.00")

nota50 = centavos // 5000
centavos %= 5000
print(f"{nota50} nota(s) de R$ 50.00")

nota20 = centavos // 2000
centavos %= 2000
print(f"{nota20} nota(s) de R$ 20.00")

nota10 = centavos // 1000
centavos %= 1000
print(f"{nota10} nota(s) de R$ 10.00")

nota5 = centavos // 500
centavos %= 500
print(f"{nota5} nota(s) de R$ 5.00")

nota2 = centavos // 200
centavos %= 200
print(f"{nota2} nota(s) de R$ 2.00")

# ... continue avec 2000, 1000, 500, 200

print("MOEDAS:")
# ... 100, 50, 25, 10, 5, 1 centimes

moeda = centavos // 100
centavos %= 100
print(f"{moeda} moeda(s) de R$ 1.00")

moeda1 = centavos // 50
centavos %= 50
print(f"{moeda1} moeda(s) de R$ 0.50")

moeda2 = centavos // 25
centavos %= 25
print(f"{moeda2} moeda(s) de R$ 0.25")

moeda3 = centavos // 10
centavos %= 10
print(f"{moeda3} moeda(s) de R$ 0.10")

moeda4 = centavos // 5
centavos %= 5
print(f"{moeda4} moeda(s) de R$ 0.05")

moeda5 = centavos // 1
centavos %= 1
print(f"{moeda5} moeda(s) de R$ 0.01")

