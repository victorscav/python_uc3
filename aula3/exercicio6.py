palavra = input("Digite a palavra: ")

def verificar_palindromo(palavra):
    if palavra == palavra[::-1]:
        return True    
    
    else:
        return False
    
print(verificar_palindromo(palavra))