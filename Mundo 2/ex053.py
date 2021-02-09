# Desafio 53
# Lê um texto e verifica se ele é palindromo
textopuro = str(input("Digite o texto: ")).strip()
textoagrupado = textopuro.split()
textoagrupado = ''.join(textopuro)
if textoagrupado == textoagrupado[::-1]:
    print("É um palíndromo!!!")
    print(f"''{textopuro}'' é igual de trás pra frente.")
else:
    print("Não é Palíndromo!")
    
