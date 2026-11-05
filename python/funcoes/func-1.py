# O que são funções em Python?
# Funções são blocos de código reutilizáveis que realizam uma tarefa específica. Elas permitem organizar o código, evitar repetição e melhorar a legibilidade. Em Python, as funções são definidas usando a palavra-chave "def" seguida do nome da função e parênteses.

# entrada: parâmetros ou argumentos que a função pode receber para realizar sua tarefa
# processamento: o código dentro da função que realiza a tarefa desejada    
# saída: o resultado ou valor que a função retorna após a execução do processamento

def exibir_mensagem():
    print("Olá, mundo!")
exibir_mensagem()  # Chama a função para exibir a mensagem "Olá, mundo!"

def exibir_mensagem_2(nome):
    print(f"Olá, {nome}!")
exibir_mensagem_2(nome="Fernanda")  # Chama a função passando o argumento "Fernanda" para exibir a mensagem personalizada

# args e kwargs são formas de passar um número variável de argumentos para uma função. 
# args é usado para passar uma lista de argumentos posicionais. *args -> tupla
# kwargs é usado para passar um dicionário de argumentos nomeados. **kwargs -> dicionário

def exibir_mensagem_3(*args, **kwargs):
    for arg in args:
        print(f"Argumento posicional: {arg}")
    for key, value in kwargs.items():
        print(f"Argumento nomeado: {key} = {value}")

exibir_mensagem_3("Alice", "Bob", nome="Carol", idade=30)  # Chama a função passando argumentos posicionais e nomeados  