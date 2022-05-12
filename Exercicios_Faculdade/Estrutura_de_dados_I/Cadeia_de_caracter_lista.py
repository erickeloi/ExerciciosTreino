class Lista:
    def __init__(self):
        self.MaxTam = 1000
        self.items = []
        self.Primeiro = 0
        self.Ultimo = 0


def Vazia(lista: Lista):
    if lista.Primeiro == lista.Ultimo:
        return True
    else:
        return False
    
def FLVazia(lista: Lista):
    lista.Primeiro = 0
    lista.Ultimo = lista.Primeiro
    lista.items = []

def insere(valor: str, lista: Lista):
    if lista.Ultimo == lista.MaxTam:
        print("A lista está cheia, não é possível adicionar mais itens")
    else:
        lista.items[lista.Ultimo] = valor
        lista.Ultimo += 1
        
# INACABADO
def retira(lista: Lista, indice: int):
    if Vazia(lista):
        print("Lista Vazia, Não é possível remover itens!")
    else:
        item_removido = lista.items[indice]
        lista.items -= lista.items[indice]
        return item_removido
    

