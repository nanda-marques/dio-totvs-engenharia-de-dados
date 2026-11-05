# tuplas são imutáveis, ou seja, não podem ser modificadas após a criação
# tuplas são representadas por parênteses () e os elementos são separados por vírgula
# exemplo de tupla      
tupla = (1, 2, 3, "quatro", "cinco", 6.0, True, [7, 8, 9], {"chave": "valor"},)
print(tupla)  # Imprime a tupla completa
print(tupla[0])  # Acessa o primeiro elemento da tupla (1)
print(tupla[-1])  # Acessa o último elemento da tupla ({"chave": "valor"})
print("----------------------------------")
("----------------------------------")
frutas = ()
print(frutas)  # Imprime a tupla vazia

len(frutas)  # Retorna o número de elementos na tupla (0)

carros = ("gol") 
print(isinstance(carros, tuple)) 
# Imprime False, pois "gol" é uma string, não uma tupla