class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


# ate as 8:00
class Fila():
    def __init__(self):
        self._size = 0

        self.first = None
        self.last = self.first
    
    def enfileira(self, elemento):
        node = Node(elemento)

        if self.last == None:
            self.last = node

        else:
            self.last.next = node
            self.last = node
            
        if self.first == None:
            self.first = node

        self._size += 1

    def pop(self):
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
        """Insere um elemento no começo da fila"""
        node = Node(data)

        aux_pointer = self.first
        self.first = node
        self.first.next = aux_pointer

        self._size += 1
            
    def __str__(self):
        r = ""
        pointer = self.first
        while(pointer):
            r = r + f'{pointer.data}' + " "
            pointer = pointer.next

        return r   

    def mostra_fila(self):
        r = ""
        pointer = self.first
        while(pointer):
            r = r + f'{pointer.data}' + " "
            pointer = pointer.next

        return r            

    def __len__(self):
        return self._size

fila = Fila()
fila.enfileira(1)
fila.enfileira(2)
fila.enfileira(3)
print(fila)

fila.fura_fila(5)
print(fila)

fila.pop()
print(fila)
