# Desafio 22
# Lê o nome completo de uma pessoa e mostra:
# O nome com letras maiúsculas, o nome com letras minúsculas,
# Quantas letras no total (sem considerar os espaços)
# Quantas letras tem o primeiro nome

nome = str(input("Digite aqui seu nome completo: "))
nomejunto = nome.replace(' ', '')
print(f"Seu nome em letras MAIÚSCULAS é: {nome.upper()}")
print(f"Seu nome em letras minúsculas é: {nome.lower()}")
print(f"Seu nome possui {len(nomejunto)} letras, desconsiderando os espaços")
print(f"Seu primeiro nome é {nome.split()[0]} e ele possui {len(nome.split()[0])} letras")
