# Lê a linha de entrada contendo nomes separados por vírgula e espaço
entrada = input()

# TODO: Para cada nome, remova espaços extras e transforme em maiúsculas
# Dica: Use split(',') para separar os nomes e depois aplique strip() e upper() em cada um

clientes = entrada.split(",")
clientes = [cliente.strip().upper() for cliente in clientes]

# Exemplo de saída esperada: 'ANA; BRUNO; CARLA'
print(f"{'; '.join(clientes)}")
