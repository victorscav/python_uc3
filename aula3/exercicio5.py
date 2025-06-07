# Conte quantas vezes o usuario interagiu ate digitar a opcao de sair, utilize funcao, while e crie um menu com 3 opçoes


menu = ["1. Lista", "2. Produto", "3. Sair"]

contador = 0
while True:
    print(menu)
    numero = int(input("Digite o número da opção desejada: "))
    if numero == 3:
        print(f"{contador}")
        break
    else:
        contador = contador + 1
