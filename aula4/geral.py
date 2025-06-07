import random
# Armazene 5 frutas nas 4 estruturas (Lista/Set/Tupla/Dict)

# definir uma lista vazia

listavazia = []

# criar uma estrutura de repetição para inserir os 5 elementos

#for i in range(5):
 #   fruta = input(f"Informe a {i + 1} fruta: ")
 #   listavazia.append(fruta)
 
def gerar_dados(qtd, valormin, valormax):
    return [random.randint(valormin, valormax) for _ in range(qtd)]

listavazia = gerar_dados(8, 1, 50)

        

# criar uma variável para cada estrutura e fazer a devida conversão

lista_final =  list(listavazia)
set_final = set(listavazia)
tupla_final = tuple(listavazia)
dict_final = {j: valor for j, valor in enumerate(listavazia)}

# imprimir os 5 resultados

print(f"Lista {lista_final}")
print(f"Set {set_final}")
print(f"Tupla {tupla_final}")
print(f"Dicionário {dict_final}")


# 2- Após o teste acima, aplique o random para inserir os valores na lista




