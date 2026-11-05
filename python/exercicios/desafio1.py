# Lê a linha de entrada e separa os valores
entrada = input().strip().split()
valor_total = float(entrada[0])
percentual_desconto = int(entrada[1])

# Calcula o valor final
valor_final = valor_total * (1 - percentual_desconto / 100)

# Imprime com duas casas decimais
print(f"{valor_final:.2f}")