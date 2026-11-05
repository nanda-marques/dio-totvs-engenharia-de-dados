lista = [1, "dois", 3.0, True, [4, 5], {"seis": 6}]

l2 = lista.copy()  # Retorna uma cópia da lista
print(lista)  # Imprime a lista original
print(l2)  # Imprime a cópia da lista

print(id(lista))  # Imprime o endereço de memória da lista original
print(id(l2))  # Imprime o endereço de memória da cópia da lista (diferente da lista original)

cores = ["vermelho", "verde", "azul"]
print(cores)  # Imprime a lista de cores

count = cores.count("verde")  # Conta quantas vezes "verde" aparece na lista
print(count)  # Imprime o resultado da contagem (1)

linguagens = ["Python", "Java", "C++", "Python", "JavaScript, C++"]
print(linguagens)  # Imprime a lista de linguagens de programação

linguagens.extend(["Ruby", "Go"])  # Adiciona os elementos "Ruby" e "Go" ao final da lista
print(linguagens)  # Imprime a lista de linguagens de programação atualizada    

print(linguagens.index("C++"))  # Imprime o índice do primeiro elemento "C++" na lista (2)

linguagens.pop()  # Remove e retorna o último elemento da lista (Go)
print(linguagens)  # Imprime a lista de linguagens de programação atualizada

linguagens.remove("Python")  # Remove a primeira ocorrência de "Python" da lista
print(linguagens)  # Imprime a lista de linguagens de programação atualizada

linguagens.reverse()  # Inverte a ordem dos elementos na lista

linguagens = ["python", "js", "c", "java", "csharp"]

sorted(linguagens, key=lambda x: len(x)) # ["c", "js", "java", "python", "csharp"]

sorted(linguagens, key=lambda x: len(x), reverse=True) # ["python", "csharp", "java", "js", "c"]

# lambda é uma função anônima, ou seja, uma função sem nome, que pode ser definida em uma única linha. Ela é frequentemente usada como argumento para funções de ordem superior, como sorted(), map(), filter(), etc. No exemplo acima, a função lambda recebe um argumento x e retorna o comprimento da string x (len(x)). O sorted() usa essa função lambda para ordenar as linguagens de programação com base no comprimento de seus nomes.

print([n**2 if n > 6 else n for n in range(10) if n % 2 == 0])