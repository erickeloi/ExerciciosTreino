# Desafio 25
# Lê um nome e identifica se tem 'SILVA' nele
print(" ' True ' se tiver 'Silva'\n ' False ' se não tiver 'Silva' ")
nome = input("Digite aqui o nome: ")
nome = nome.lower().strip()
print(f"Tem 'Silva' no nome? {'silva' in nome}")

