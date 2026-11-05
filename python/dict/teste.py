carro = {
    "marca": "Fiat", "modelo": "palio", "placa": "ABD-9826"
    }
print(carro.get("pais"))
print(carro.get("marca"))

contatos = {"idioma": "pt_br", "pais": "Brasil" }

print(contatos.get("idioma"))  # Retorna o valor associado à chave "idioma" (pt_br)
print(contatos.get("pais"))  # Retorna o valor associado à chave "pais" (Brasil)
print(contatos.get("cidade", "Chave não encontrada"))  # Tenta acessar a chave "cidade", mas como ela não existe, retorna a mensagem "Chave não encontrada"

