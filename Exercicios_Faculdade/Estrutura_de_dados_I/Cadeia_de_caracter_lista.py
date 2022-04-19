class Lista:
    def __init__(self):
        self.MaxTam = 1000
        
        self.Primeiro = 0
        self.Ultimo = 0
        
        self.items = []

def Vazia(lista: Lista):
    if lista.Primeiro == lista.Ultimo:
        return True
    else:
        return False
    
def FLVazia(lista: Lista):
    lista.Primeiro = lista.Ultimo
    lista.items = []

def insere(valor: str, lista: Lista):
    if lista.Ultimo == lista.MaxTam:
        print("A lista está cheia, não é possível adicionar mais itens")
    else:
        lista.items[lista.Ultimo] = valor
        lista.Ultimo += 1

def retira(self)
        
        
        
        
