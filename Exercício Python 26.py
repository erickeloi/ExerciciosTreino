# Desafio 26 
# Lê um nome e identifica quantas vezes aparece a letra 'a' nele, quando aparece primeiro, quando aparece por último
nome = str(input("Digite aqui o nome: ")).strip()
print(f"A letra 'a' aparece {nome.lower().count('a')} vezes no nome '{nome}'.")
print(f"Ela aparece primeiro na posição {nome.lower().find('a')+1} e por último na posição {nome.lower().rfind('a')+1}")
