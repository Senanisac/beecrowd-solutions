
nome = str(input())
salario = float(input())
vendas = float(input())

comissao = (vendas * 15) / 100
total = comissao + salario

print(f"TOTAL = R$ {total:.2f}")

