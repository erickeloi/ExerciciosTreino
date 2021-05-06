# Exercício Python 080:
# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort() ).
# No final, mostre a lista ordenada na tela.


lista_valores = list()
valor_digitado = valor_maximo = valor_minimo = 0

while len(lista_valores) != 5:

    valor_digitado = int(input("Digite um valor: "))

    if len(lista_valores) == 0:
        valor_minimo = valor_digitado

    if valor_digitado < valor_minimo:
        valor_minimo = valor_digitado
        print(f"Adicionando o valor {valor_digitado} no inicio da lista...")
        lista_valores.insert(0, valor_digitado)

    elif valor_maximo > valor_digitado > valor_minimo:
        print("Inserindo valor no meio da lista...")
        lista_valores.insert((len(lista_valores))//2, valor_digitado)
        # Problemas se o ultimo número for maior que o do meio e o segundo numero for menor que o ultimo
        
    elif valor_digitado > valor_maximo:
        valor_maximo = valor_digitado
        print(f"Adicionando o valor {valor_digitado} no fim da lista...")
        lista_valores.append(valor_digitado)

print(f"A lista digitada foi {lista_valores}")


# Versão do Gustavo Guanabara:

# lista = []
# for i in range(0, 5):
#     n = int(input("Digite um número: \n"))
#     if i  == 0 or n > lista[-1]:
#       lista.append(n)
#     else:
#       pos = 0
#       while pos < len(lista):
#         if n <= lista[pos]:
#           lista.insert(pos, n)
#           break
#         pos += 1
# print(lista)
