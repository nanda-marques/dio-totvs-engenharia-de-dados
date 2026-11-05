contatos = {
    "marxsnanda07@gmail.com": {"nome": "Fernanda", "telefone": "11 123456789"},
    "maria@outlook.com": {"nome": "Maria", "telefone": "11 987654321", "extra": {"endereco": "Rua das Flores, 123", "cidade": "São Paulo"}},
}

copy = contatos.copy()  # Retorna uma cópia do dicionário
print(contatos)  # Imprime o dicionário original
print("------------")
copy["marxsnanda07@gmail.com"]["telefone"] = "11 999999999"  # Modifica o número de telefone de Fernanda na cópia
print(copy)  # Imprime a cópia do dicionário com o número de telefone atualizado
print("------------")
dict.fromkeys(["chave1", "chave2", "chave3"], "valor padrão")  # Cria um novo dicionário com as chaves especificadas e um valor padrão para todas as chaves

contatos.clear()  # Remove todos os itens do dicionário
print(contatos)  # Imprime o dicionário vazio
print("------------")

print(copy.get("chave"))
# Tenta acessar a chave "chave" na cópia do dicionário, mas como ela não existe, retorna None
print(copy.get("chave", {}))
# Tenta acessar a chave "chave" na cópia do dicionário, mas como ela não existe, retorna um dicionário vazio {}
print(copy.get("marxsnanda07@gmail.com", {}))
# Tenta acessar a chave "marxsnanda07@gmail.com" na cópia do dicionário

copy.items()  # Retorna uma visão dos itens (pares chave-valor) do dicionário como uma lista de tuplas

