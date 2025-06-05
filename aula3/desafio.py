# crie uma funcao para imprimir um quadrado de asteristicos


tamanho = int(input("Digite o tamanho desejado: "))

def parte_um(tamanho):
    for i in range(tamanho):
        print("*" * tamanho)

#parte_um(tamanho)

def parte_dois(tamanho):
    meio = tamanho // 2
    for i in range(tamanho):
        linha = ''
        for j in range(tamanho):
            if i == meio and j == meio:
                linha += ' '
            else:
                linha += '*'
        print(linha)

#parte_dois(tamanho)

def parte_tres(tamanho):
    
    altura = tamanho // 2
    for i in range(altura + 1):
        espacos = ' ' * (altura - i)
        asteristicos = '*' * (2 * i + 1)
        print(espacos + asteristicos + espacos)
        
parte_tres(tamanho)
