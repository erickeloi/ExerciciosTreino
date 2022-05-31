class Node():
    """ Nós, que vão encadear a fila"""
    def __init__(self, data):
        self.data = data
        self.next = None

class Fila():
    """ Estrutura de dados 'FILA'/'QUEUE' """
    def __init__(self):
        self._size = 0

        self.first = None
        self.last = self.first
    
    def enfileira(self, elemento):
        """ Basicamente função 'PUSH', insere um elemento no fim da fila"""
        node = Node(elemento)

        if self.last == None:
            self.last = node

        else:
            self.last.next = node
            self.last = node
            
        if self.first == None:
            self.first = node

        self._size += 1

    def desenfileira(self):
        """ Basicamente função 'POP', tira o elemento do começo da fila"""
        if self.first != None:
            elem = self.first.data 
            self.first = self.first.next

            self._size -= 1

            return elem
        else:
            print("Erro! Pilha Vazia")

        # implementar def fura fila:
        # colocar um no começo da fila usando alocação dinamica
    def fura_fila(self, data):
        """ Insere um elemento no começo da fila """
        node = Node(data)

        aux_pointer = self.first
        self.first = node
        self.first.next = aux_pointer

        self._size += 1
            
    #def __str__(self):
    #""" Mostra a pilha ao usuário ao usar a função print() na classe """
    #    r = ""
    #    pointer = self.first
    #    while(pointer):
    #        r = r + "" + f'{pointer.data}' + " "
    #        pointer = pointer.next
    #    return r   

    def mostra_fila(self):
        """ Mostra a pilha ao usuário, Basicamente a função Print """
        r = ""
        pointer = self.first
        while(pointer):
            r = r + "" + f'{pointer.data}' + " "
            pointer = pointer.next
        print(r)          

    def __len__(self):
        """ Mostra o tamanho da fila ao usar a função len() na fila """
        return self._size

fila = Fila()
fila.enfileira(1)
fila.enfileira(2)
fila.enfileira(3)
fila.mostra_fila()

fila.fura_fila(5)
fila.mostra_fila()

fila.desenfileira()
fila.mostra_fila()

print(f"A fila possui: {len(fila)} elemento(s)")
