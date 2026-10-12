
# Lê a primeira linha: código, quantidade, valor unitário
codigo1, qtd1, valor1 = input().split()

# Lê a segunda linha: código, quantidade, valor unitário
codigo2, qtd2, valor2 = input().split()

# Converte para os tipos apropriados
qtd1 = int(qtd1)
valor1 = float(valor1)
qtd2 = int(qtd2)
valor2 = float(valor2)

# Calcula o total
total = qtd1 * valor1 + qtd2 * valor2

# Mostra o resultado com 2 casas decimais
print(f"VALOR A PAGAR: R$ {total:.2f}")

