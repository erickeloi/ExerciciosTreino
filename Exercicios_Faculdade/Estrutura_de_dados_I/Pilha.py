class Pilha():
    def __init__(self):
        self.topo = 0
        self.elementos = []
    def insere(self, elemento):
        self.elementos += [elemento]
        self.topo += 1
    def imprimir(self):
        contador = 0
        while contador != self.topo:
            print(self.elementos[contador], end= ' ')
            contador += 1 
        print()
    def isPilhaVazia(self):
        return pilha == []
    def pop(self):
        if self.isPilhaVazia():
            print("Erro! Pilha Vazia")
        else:
            aux = self.elementos[-1]
            self.elementos = self.elementos[:-1]
            self.topo -= 1
            return aux
    def inverter_palavra(self, palavra):
        palavra = list(palavra)
        palavra_invertida = ""
        for letra in palavra[::-1]:
            palavra_invertida += "" + letra

        return palavra_invertida

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

    def new_mostrar_palavras_invertida(self):
        frase_completa = self.elementos[0] + " "
        frase_completa = list(frase_completa)
        palavra_invertida = ""
        palavra_aux = ""
        for elemento in frase_completa:
            if elemento != " ":
                palavra_aux += elemento
            elif elemento == " " or elemento == frase_completa[-1]:
                palavra_invertida += " " + self.inverter_palavra(palavra_aux)
                palavra_aux = ""

        return palavra_invertida

    def elementos_invertidos(self):
        return self.elementos[::-1]


def inverte_com_pilha(palavra: str):
    pilha = Pilha()
    palavra = list(palavra)
    palavra_invertida = ""
    # SOLUÇÃO 2
    for letra in palavra:
        pilha.insere(letra)
    
    contador = pilha.topo - 1
    while contador != 0:
        palavra_invertida += pilha.pop()
        contador -= 1
    return palavra_invertida
    # SOLUÇÃO 1
    #for letra in palavra:
    #    pilha.insere(letra)

    #contador = pilha.topo -1
    #while contador != -1:
    #    palavra_invertida += pilha.elementos[contador]
    #    contador -= 1
    
    #return palavra_invertida




def dec_to_bin(numero: int):
    if numero < 0:
        print("Erro: O Número deve ser maior que zero!")
    else:
        restos = Pilha()
        while True:
            resto = numero % 2
            numero = numero // 2

            restos.insere(resto)

            if numero == 1:
                restos.insere(1)
                return restos.elementos_invertidos()
            

print(dec_to_bin(10))      

pilha = Pilha()

pilha.insere("ESTE EXERCICIO E MUITO FACIL")
#pilha.insere('ESTE')
#pilha.insere('EXERCICIO')
#pilha.insere('E')
#pilha.insere('MUITO')
#pilha.insere('FACIL')
#print("Mostrando os elementos da pilha... ")
#pilha.imprimir()
#print("Invertendo as Palavras da pilha... ")

#print(pilha.new_mostrar_palavras_invertida())

#print("Invertendo UMA palavra: ")
#print(pilha.inverter_palavra('ESTE'))
#print(pilha.invertido())
#print(f"Desempilhando... (pop): {pilha.pop()}")

print(inverte_com_pilha('exemplo'))
