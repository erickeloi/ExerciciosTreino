# Desafio 65
# Lê vários números inteiros e no final mostra a media, maior e menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar digitando os valores.
num = 0
medianum = 0
soma = 0
maior = 0
menor = 0
continuar = ''
contador = 0
while continuar != 'F':
    contador +=1
    num = int(input("Digite um número: "))
    if contador == 1:
        maior = num
        menor = num
    if num > maior:
        maior = num
    if num < maior:
        menor = num
    soma = num + soma
    continuar = str(input("Digite ' F ' para parar o programa ou qualquer coisa para continuar: ")).upper().strip()
medianum = soma / contador
print(f" Então, a média desses números é {medianum},\nO maior número digitado é o {maior}\nE o menor número digitado foi o {menor}")
