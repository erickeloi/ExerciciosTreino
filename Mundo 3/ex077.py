# Exercício Python 76 
# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ("coisa", "casa", "tempo", "ano", "dia", "vez", "homem", "senhor", "senhora", "moço", "moça")

for palavra in palavras:
    print(f"As vogais da palavra '{palavra.title()}' são: ",end="")
    if "a" in palavra:
        print(f"a ", end="")
    if "e" in palavra:
        print(f"e ", end="")
    if "i" in palavra:
        print(f"i ", end="")
    if "o" in palavra:
        print(f"o ", end="")
    if "u" in palavra:
        print(f"u", end="")
    print(" ")

