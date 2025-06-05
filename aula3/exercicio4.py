# Imprima uma tabuada escolhida pelo usuario, utilize time, funcao e for

import time
numero = int(input("Tabuada do número: "))

def tabuada(numero):
    for i in range(0,11):
        print((f"{numero} x {i} = {numero * i}"))
        time.sleep(1)

tabuada(numero)