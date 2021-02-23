# Exercício 72
# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
Numbers = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
option = int(input("Digite um número ( de 0 a 20 )para saber como escrevê-lo por extenso: "))
while option not in range(0, 21):
    print("Digite uma opção válida!")
    option = int(input("Digite um número ( de 0 a 20 )para saber como escrevê-lo por extenso: "))
print(f"O número {option} escrito por extenso é: {Numbers[option]}")
