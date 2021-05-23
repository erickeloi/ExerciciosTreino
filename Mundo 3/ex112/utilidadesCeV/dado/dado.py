# Exercício Python 112: Entrada de dados monetários
# Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado.
# Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(),
# mas com uma validação de dados para aceitar apenas valores que seja monetários.


def leiaDinheiro():
    while True:
        print("Digite o valor monetário: ", end="")
        numero = str(input()).strip()
        lista = list(numero)
        lista_de_numeros = list()
        elemento_juntado = ""

        if numero.isascii():

            for elemento in lista:

                if str(elemento).isnumeric():
                    lista_de_numeros.append(elemento)
                elif elemento == "," or elemento == ".":
                    if elemento == ",":
                        elemento = "."
                    lista_de_numeros.append(elemento)

                else:
                    print(f"O elemento \"{elemento}\" será desconsiderado")

        else:
            print("Erro! Entrada inválida, tente novamente! ")

        if len(lista_de_numeros) == 0:
            print("Erro! Entrada inválida, tente novamente!")

        else:
            elemento_juntado = "".join(lista_de_numeros)
            if float(elemento_juntado):
                elemento_juntado = float(elemento_juntado)
                return elemento_juntado
            else:
                print("Erro! Entrada inválida, tente novamente")
