# Dicionário - coleção de pares chave-valor, onde cada chave é única e está associada a um valor.
# Dicionários são representados por chaves {} e os pares chave-valor são separados por vírgula, com a chave e o valor separados por dois pontos (:)

# exemplo de dicionário

pessoa = {
    "nome": "Fernanda",
    "idade": 18,
    "cidade": "São Paulo"
}

pessoa = dict(nome="Fernanda", idade=18, cidade="São Paulo")
print(pessoa)  # Imprime o dicionário completo  

pessoa["profissao"] = "estudante"  # Adiciona um novo par chave-valor ao dicionário
print(pessoa)  # Imprime o dicionário atualizado com a nova chave "profissao"

print(pessoa["nome"])  # Acessa o valor associado à chave "nome" (Fernanda)
print(pessoa.get("idade"))  # Acessa o valor associado à chave "idade" (18)
print(pessoa.get("altura", "Chave não encontrada"))  # Tenta acessar a chave "altura", mas como ela não existe, retorna a mensagem "Chave não encontrada"

pessoa["nome"] = "Fernanda Marques" # Modifica o valor associado à chave "nome"

contatos = {
    "marxsnanda07@gmail.com": {"nome": "Fernanda", "telefone": "11 123456789"},
    "maria@outlook.com": {"nome": "Maria", "telefone": "11 987654321", "extra": {"endereco": "Rua das Flores, 123", "cidade": "São Paulo"}},
}

telefone_fernanda = contatos["marxsnanda07@gmail.com"]["telefone"]  # Acessa o número de telefone associado à chave "marxsnanda07@gmail.com" e à chave "telefone"
print(telefone_fernanda)  # Imprime o número de telefone de Fernanda

extra = contatos["maria@outlook.com"]["extra"]  # Acessa o dicionário aninhado associado à chave "maria@outlook.com"
print(extra)  # Imprime o dicionário de informações extras de Maria

for chave in contatos:
    print(chave, contatos[chave])  # Imprime cada chave do dicionário "contatos"

for lugar in contatos:
    print(lugar, contatos[lugar])  # Imprime cada chave do dicionário "contatos" (lugar) e o valor associado a essa chave (informações de contato)