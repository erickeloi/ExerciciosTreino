# Exercício Python 76
# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

lista = ('lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20,
         'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('-='*20)
print(f"{'Listagem de Preços!':^40}")
print('-='*20)
for item in lista:
    if type(item) == str:
        print("{:.<20}".format(item), end='')
    if type(item) == float:
        print(f"{item:.2f}")
