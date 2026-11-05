nome = "Fernanda Marques"

nome_completo = nome[0:9]  # Fatiamento do nome (do índice 0 ao 8)
sobrenome = nome[9:17]      # Fatiamento do sobrenome (do índice 10 ao 16)
print("Nome:", nome_completo)
print("Sobrenome:", sobrenome)

print(nome[::-1])  # Fatiamento com passo -1 (inversão da string)