# parametros especiais 
# positional only -> / -> os parâmetros antes da barra (/) só podem ser passados por posição, ou seja, sem usar o nome do parâmetro
# keyword only -> * -> os parâmetros após o asterisco (*) só podem ser passados por nome, ou seja, usando o nome do parâmetro

def funcao_exemplo(a, b, /, c, d, *, e, f):
    print(f"a: {a}, b: {b}, c: {c}, d: {d}, e: {e}, f: {f}")
funcao_exemplo(1, 2, 3, 4, e=5, f=6)  # Chama a função passando os argumentos de acordo com as regras de parâmetros posicionais e nomeados  
funcao_exemplo(1, 2, c=3, d=4, e=5, f=6)  # Chama a função passando os argumentos de acordo com as regras de parâmetros posicionais e nomeados  

#escopo local e global
# variáveis definidas dentro de uma função têm escopo local e só podem ser acessadas dentro dessa função, enquanto variáveis definidas fora de qualquer função têm escopo global e podem ser acessadas em qualquer parte do código.

salario = 5000  # Variável global

def calcular_imposto(bonus):
    global salario  # Indica que a variável 'salario' dentro da função se refere à variável global
    salario += bonus  # Variável local

print(salario)  # Imprime o valor do salário antes de chamar a função (5000)
calcular_imposto(1000)  # Chama a função para calcular o imposto, passando um bônus de 1000
print(salario)  # Imprime o valor do salário após chamar a função (6000)


#  Em Python podemos atribuir funções a variáveis, passá-las como parâmetro para outras funções e usar como valor de retorno para uma função.

def funcao(*args, **kw):
    funcao("python", 2022, curso="dio")

print(funcao)  # Imprime o nome da função (funcao)

