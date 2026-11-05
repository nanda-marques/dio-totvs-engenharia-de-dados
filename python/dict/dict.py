dicionario = {
    'nome': 'João', 'idade': 30, 'cidade': 'São Paulo',
    'nome': 'Maria', 'idade': 25, 'cidade': 'Rio de Janeiro'
}
dicionario['nome'] = 'Maria'
dicionario['idade'] = 25
dicionario['cidade'] = 'Rio de Janeiro'


clear = dicionario.clear()  # Remove todos os itens do dicionário
print(dicionario)  # Imprime o dicionário vazio

dicionario.get('nome')  # Retorna o valor associado à chave 'nome' ou None se a chave não existir
dicionario.get('sobrenome', 'Chave não encontrada')  # Retorna o valor associado à chave 'sobrenome' ou a mensagem 'Chave não encontrada' se a chave não existir

dicionario.items()  # Retorna uma visão dos itens (pares chave-valor) do dicionário como uma lista de tuplas
dicionario.keys()  # Retorna uma visão das chaves do dicionário

dicionario.values()  # Retorna uma visão dos valores do dicionário

novo_dicionario = dict.fromkeys(['chave1', 'chave2', 'chave3'], 'valor padrão')  # Cria um novo dicionário com as chaves especificadas e um valor padrão para todas as chaves
print(novo_dicionario)  # Imprime o novo dicionário criado com as chaves e o valor padrão

novo_dicionario.pop('chave1')  # Remove a chave 'chave1' do dicionário e retorna seu valor
print(novo_dicionario)  # Imprime o dicionário após a remoção

novo_dicionario.popitem()  # Remove e retorna um par chave-valor aleatório do dicionário
print(novo_dicionario)  # Imprime o dicionário após a remoção

novo_dicionario.setdefault('chave4', 'valor padrão')  # Retorna o valor da chave 'chave4' se ela existir, caso contrário, adiciona a chave com o valor 'valor padrão' e retorna esse valor
print(novo_dicionario)  # Imprime o dicionário após a adição

novo_dicionario.update({'chave5': 'novo valor', 'chave6': 'outro valor'})  # Atualiza o dicionário com os pares chave-valor do dicionário fornecido
print(novo_dicionario)  # Imprime o dicionário atualizado com as novas chaves e valores

novo_dicionario.values()  # Retorna uma visão dos valores do dicionário atualizado

"chave1" in novo_dicionario  # Verifica se a chave 'chave1' existe no dicionário e retorna True ou False

resultado = "chave2" in novo_dicionario  # Verifica se a chave 'chave2' existe no dicionário e armazena o resultado (True ou False) na variável 'resultado'


lista_chaves: list = list(novo_dicionario.keys())  # Converte as chaves do dicionário em uma lista

del novo_dicionario['chave5']  # Remove a chave 'chave5' do dicionário
print(novo_dicionario)  # Imprime o dicionário após a remoção

del novo_dicionario  # Exclui completamente o dicionário da memória