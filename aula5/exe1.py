# Funções - Manipulação de arquivos
# Criar uma função que cria e adiciona um texto no arquivo

def criar_arquivo(nome_arquivo: str, conteudo: str):
    """Cria um arquivo com o nome e conteúdo fornecidos."""
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(conteudo)
        print("Arquivo criado com sucesso!")

#nome = input("Digite o nome do arquivo: ")
#criar_arquivo (f"./aula5/arquivos/{nome}.txt", "Este é um exemplo de arquivo criado com Python.")

# Ler o arquivo

def ler_arquivo(nome_arquivo: str):
    """Retorna o conteúdo de um arquivo."""
    with open(nome_arquivo, 'r') as arquivo:
        return arquivo.read()

#nome = input("Digite o nome do arquivo: ")
#print(ler_arquivo(f"./aula5/arquivos/{nome}.txt"))

# Adicionar conteúdo

def adicionar_conteudo(nome_arquivo: str, conteudo: str):
    """Adicionar um conteúdo ao final de um arquivo."""
    with open(nome_arquivo, 'a') as arquivo:
        arquivo.write("\n" + conteudo)
        print("Conteúdo adicionado com sucesso!")

#nome = input("Digite o nome do arquivo: ")
#conteudo = input("Digite o conteúdo desejado: ")
#adicionar_conteudo(f"./aula5/arquivos/{nome}.txt", conteudo)

# Remover arquivo
import os

def remover_arquivo(nome_arquivo: str):
    """Remover um arquivo se ele existir."""
    if os.path.exists(nome_arquivo):
        os.remove(nome_arquivo)
        (print("Arquivo removido com sucesso!"))
    else:
        print("Arquivo não encontrado!")

#nome = input("Digite o nome do arquivo: ")
#remover_arquivo(f"./aula5/arquivos/{nome}.txt")

# Contar linhas

def contar_linhas(nome_arquivo: str) -> int:
    """Retorna a quantidade de linhas de um arquivo."""
    with open(nome_arquivo, 'r') as arquivo:
        return len(arquivo.readlines())
    
#nome = input("Digite o nome do arquivo: ")
#print(contar_linhas(f"./aula5/arquivos/{nome}.txt"))

# Verificar se uma palavra existe no conteúdo

def ver_palavra(nome_arquivo: str, palavra:str) -> bool:
    """Verifica se a palavra existe no arquivo."""
    with open(nome_arquivo, "r") as arquivo:
        return palavra in arquivo.read()
        
#palavrav = input("Digite a palavra que deseja verificar: ")
#nome = input("Digite o nome do arquivo: ")
#print(ver_palavra(f"./aula5/arquivos/{nome}.txt", palavrav))

# Criar um arquivo com 3 linhas contendo um número em cada linha

def criar_arquivolinha(nome_arquivo: str, conteudo: str):
    """Cria um arquivo com o nome e conteúdo fornecidos."""
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(conteudo)
        print("Arquivo criado com sucesso!")

#nome = input("Digite o nome do arquivo: ")
#criar_arquivolinha (f"./aula5/arquivos/{nome}.txt", "1\n2\n3")

# Criar uma função que soma os números desse arquivo

def soma_numeros(nome_arquivo:str) -> int:
    """Retorna a soma dos números de um arquivo."""
    with open(nome_arquivo, "r") as arquivo:
        return sum(int(linha.strip()) for linha in arquivo)
    
#nome = input("Digite o nome do arquivo: ")
#print(soma_numeros(f"./aula5/arquivos/{nome}.txt"))

# Atualiza uma linha específica do arquivo

def att_linha(nome_arquivo:str, novo_conteudo:str, linha_alvo: int):
    """Atualiza uma linha específica do arquivo"""
    with open(nome_arquivo, "r") as arquivo:
        linhas = arquivo.readlines()
        if 0 <= linha_alvo < len(linhas):
            linhas[linha_alvo] = novo_conteudo + "\n"
    with open(nome_arquivo, "w") as arq:
        arq.writelines(linhas)

nome = input("Digite o nome do arquivo: ")
conteudo = input("Digite o conteúdo que deseja adicionar: ")
linha = int(input("Informe o número da linha que deseja atualizar: "))

print(att_linha(f"./aula5/arquivos/{nome}.txt", conteudo, linha))
        







