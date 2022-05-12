class Pilha():
    def __init__(self):
        self.topo = 0
        self.elementos = []
    def insere(self, elemento: str):
        self.elementos += [elemento]
        self.topo += 1
    def imprimir(self):
        contador = 0
        while contador != self.topo:
            print(self.elementos[contador], end= ' ')
            contador += 1 
        print()
    def pop(self):
        aux = self.elementos[-1]
        self.elementos = self.elementos[:-1]
        return aux
    def mostrar_palavras_invertidas(self):
        palavras_invertidas_final = []
        palavra = []
        palavra_invertida = ""
        letras = []
        contador_letras = -1
        
        lista_len = self.topo - 1
        contador = 0
        while contador <= lista_len:
            palavra = self.elementos[contador]

            for letra in palavra:
                letras += [letra]
                contador_letras += 1
            
            while contador_letras >= 0:
                palavra_invertida += letras[contador_letras]
                contador_letras -= 1

            palavras_invertidas_final += [palavra_invertida]

            palavra_invertida = ""
            contador_letras = -1
            letras = []
            contador += 1

        contador = 0
        while contador != self.topo:
            print(palavras_invertidas_final[contador], end=' ')
            contador += 1 
        print()
        

pilha = Pilha()

pilha.insere('ESTE')
pilha.insere('EXERCICIO')
pilha.insere('E')
pilha.insere('MUITO')
pilha.insere('FACIL')
print("Mostrando os elementos da pilha... ")
pilha.imprimir()
print("Invertendo as Palavras da pilha... ")
pilha.mostrar_palavras_invertidas()
print(f"Desempilhando... (pop): {pilha.pop()}")
