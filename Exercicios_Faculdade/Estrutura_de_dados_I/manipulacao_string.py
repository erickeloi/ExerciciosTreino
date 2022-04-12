# TAD - Manipulação de String
#   INTERFACES
    #   TO DO: Implementar funções de caracteres ( char, string, concatenar, copiar )

def compara(palavra1: str, palavra2: str):
    if palavra1 == palavra2:
        return True
    else:
        return False

def concatena(palavra_inicial: str, palavra_final: str):
    palavra_inicial += palavra_final
    return palavra_inicial

def copia(palavra_fonte: str, palavra_destino: str):
    palavra_destino = palavra_fonte
    return palavra_destino

def palindromo(palavra: str):
    palavra1 = palavra
    palavra2 = palavra[::-1]
    return compara(palavra1, palavra2)
    
#from TAD_CONCATENAR import *

palavra1 = "asa"
palavra2 = "asa"

print(compara(palavra1, palavra2))

print(palindromo(palavra1))
