# Imprima uma contagem regressiva com input de partida feito pelo usuário, utilize while e funcao
import time

inicial = int(input("Digite o número inicial: "))

def cont_reg(inicial):
    while inicial > 0:
            inicial = inicial - 1
            print(f"{inicial}")
            time.sleep(1)

    
cont_reg(inicial)


