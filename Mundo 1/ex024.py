# Desafio 24
# Lê um nome de uma cidade e informa se esse nome inicia ou não com a palavra "SANTO"
# Ainda sem usar a função if else, por enquanto
print(" O programa vai indicar:\n 'True' se o nome começar com 'Santo. \n 'False' se o nome não começar com 'santo'.\n")
nome = input("Digite aqui o nome da cidade: ")
nomedividido = nome.strip().lower().split()
santo = 'santo' in nomedividido[0]
print(santo)
