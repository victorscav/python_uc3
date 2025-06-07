# definir um dicionario com 3 elementos

dicionario = { "nome": "victor",
            "idade": "27",
            "cidade": "Petrópolis"}

print(dicionario)

# adicionar um elemento (chave/valor)

dicionario["profissão"] = "Programador"
print(dicionario)

# alterar um valor de uma chave específica

dicionario["idade"] = 28
print(dicionario)

# remover um elemento (chave/valor)

del dicionario["idade"]
print(dicionario)