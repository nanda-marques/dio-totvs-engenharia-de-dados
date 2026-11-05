# list - sequencia que pode conter elementos de tipos diferentes (qualquer tipo de objeto), é mutável e ordenada 
# lista é representada por colchetes [] e os elementos são separados por vírgula
# exemplo de lista
lista = [1, 2, 3, "quatro", "cinco", 6.0, True, [7, 8, 9], {"chave": "valor"}]
print(lista)  # Imprime a lista completa
print(lista[0])  # Acessa o primeiro elemento da lista (1)  
print("----------------------------------")
frutas = ["maçã", "banana", "laranja", "uva"]
print(frutas[1])  # Acessa o segundo elemento da lista (banana
print(frutas[-1])  # Acessa o último elemento da lista (uva)
print(frutas[1:3])  # Acessa os elementos do índice 1 ao 2 (banana e laranja)
print("----------------------------------")
frutas = []
print(frutas)  # Imprime a lista vazia
print("----------------------------------")
letras = list("Python")
numeros = list(range(1, 11))

print(letras)  # Imprime a lista de letras ['P', 'y', 't', 'h', 'o', 'n']
print(numeros)  # Imprime a lista de números de 1 a 

abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", 
"t", "u", "v", "w", "x", "y", "z"]

vogais = ["a", "e", "i", "o", "u"]
print(abc)  # Imprime a lista de letras do alfabeto
print(vogais)  # Imprime a lista de vogais  
consoante = [letra for letra in abc if letra not in vogais]
print(consoante)  # Imprime a lista de consoantes do alfabeto

print("----------------------------------")
numeros = [1, 30, 5, 10, 2, 8]
print(numeros)  # Imprime a lista de números
pares = [num for num in numeros if num % 2 == 0]
print(pares)  # Imprime a lista de números pares