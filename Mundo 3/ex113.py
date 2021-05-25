# Exercício Python 113: Funções aprofundadas em Python
# Reescreva a função leiaInt() que fizemos no desafio 104, 
# incluindo agora a possibilidade da digitação de um número de tipo inválido. 
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaInt():
    while True:
        try:
            numero = int(input("Digite um número inteiro: "))
            if str(numero).isnumeric():
                print(f"Você digitou o número {numero}")
                return numero
        except:
            print("Erro! Digite um número inteiro válido!")


def leiaFloat():
    while True:
        try:
            numero = float(input("Digite um número no conjunto dos Reais: "))
            if type(numero) == float:
                print(f"você digitou o número {numero}")
                return numero
        except:
            print("Erro! Digite um número no conjunto dos Reais!")


num_int = leiaInt()
num_float = leiaFloat()
print(f"Você digitou o número inteiro {num_int} e o número Real {num_float}")
