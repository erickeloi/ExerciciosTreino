# Exercício Python 104: Validando entrada de dados em Python
# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico.
# Ex: n = leiaInt('Digite um n: ')

def leiaInt():
    numero = str(input("Digite um número inteiro: "))
    if numero.isnumeric():
        print(f"Você digitou o número {numero}")    
        return numero
    else:
        print("ERRO! Digite valor apenas numerico")
        leiaInt()


leiaInt()
