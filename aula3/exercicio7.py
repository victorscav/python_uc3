termos = int(input("Digite o número de termos da sequência de Fibonacci: "))

def fibonacci(termos):
    lista = []
    a, b = 0, 1
    while len(lista) < termos:
        lista.append(a)
        a, b = b, a + b
    print(lista)

fibonacci(termos)
