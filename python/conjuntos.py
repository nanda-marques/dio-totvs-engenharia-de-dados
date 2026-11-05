# estrutura de dados - conjuntos (set) - coleção de elementos únicos, não ordenada e mutável
# conjuntos são representados por chaves {} ou pela função set() e os elementos são separados por vírgula
# exemplo de conjunto   

set([1, 2, 3, 1, 3, 4 ])
print(set([1, 2, 3, 1, 3, 4 ]))  
# Imprime o conjunto {1, 2, 3, 4} (elementos duplicados são removidos)

linguagens = {"Python", "Java", "C++", "Python", "JavaScript", "C++"}
print(linguagens)

# não suportam indexação, ou seja, não é possível acessar os elementos por meio de índices como em listas ou tuplas

# print(linguagens[0])  
# Isso resultará em um erro, pois conjuntos não são indexados (subsciptable)

carros = {"gol", "palio", "uno", "gol"}
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

# METODOS

conjunto_a = {1, 2, 3, 4}
conjunto_b = {1, 2, 3, 4, 5, 6, 7}

print(conjunto_a.union(conjunto_b))  # Retorna um novo conjunto com a união dos elementos de conjunto_a e conjunto_b

print(conjunto_a.intersection(conjunto_b))  # Retorna um novo conjunto com a inter

conjunto_a.symmetric_difference
(conjunto_b)  # Retorna um novo conjunto com os elementos que estão em conjunto_a ou conjunto_b, mas não em ambos

conjunto_a.difference(conjunto_b)  # Retorna um novo conjunto com os elementos que estão em conjunto_a, mas não em conjunto_b


print(conjunto_a.issubset(conjunto_b))
conjunto_a.issuperset(conjunto_b)  # Retorna True se conjunto_a for um superconjunto de conjunto_b, ou seja, todos os elementos de conjunto_b estão em conjunto_a

print(conjunto_a.issuperset(conjunto_b))  # Retorna True se conjunto_a for um superconjunto de conjunto_b, ou seja, todos os elementos de conjunto_b estão em conjunto_a

print(conjunto_a.isdisjoint(conjunto_b))  # Retorna True se conjunto_a e conjunto_b não tiverem elementos em comum, ou seja, a interseção dos conjuntos é vazia

1 in conjunto_a  # Retorna True se o elemento 1 estiver presente em conjunto_a, caso contrário, retorna False

len(conjunto_a)  # Retorna o número de elementos em conjunto_a (4 )