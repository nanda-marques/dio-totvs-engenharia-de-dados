# Leitura da linha de entrada
entrada = input().strip()

# TODO: Separe os campos da entrada e calcule o valor total da venda (quantidade * valor unitário)
# Dica: Use split(',') para separar os valores e int() para converter para inteiro.

produto, quantidade, valor = entrada.split(",")

produto = produto.strip()
quantidade = int(quantidade.strip())
valor = int(valor.strip())

# print(f"{produto}: {total}")  # Exemplo de saída formatada

total = quantidade * valor

print(f"{produto}: {total}")