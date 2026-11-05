nome = "Fernanda"
idade = 18
profissao = "estudante"
linguagem = "Python"
PI = 3.14159

# Interpolação moderna (str.format)
print("Meu nome é {} e tenho {} anos. Sou {} e estou aprendendo {}.".format(nome, idade, profissao, linguagem))

# Interpolação moderna (str.format) com índices
print("Meu nome é {0} e tenho {1} anos. Sou {2} e estou aprendendo {3}.".format(nome, idade, profissao, linguagem))

# Interpolação moderna (f-strings)
print(f"Meu nome é {nome} e tenho {idade} anos. Sou {profissao} e estou aprendendo {linguagem}.")

# Interpolação antiga (desaconselhada)
print("Meu nome é %s e tenho %d anos. Sou %s e estou aprendendo %s." % (nome, idade, profissao, linguagem))

print(f"O valor de PI é aproximadamente {PI:.2f}")  # Formatação para 2 casas decimais
print(f"O valor de PI é aproximadamente {PI:.4f}")  # Formatação para 4 casas decimais
print(f"O valor de PI é aproximadamente {PI:10.2}") # Formatação para 2 casas decimais e largura total de 10 caracteres (alinhado à direita)