class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class Filaa():
    def __init__(self):
        self._size = 0

        self.first = None
        self.last = None
    
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

            self._size = self._size - 1

            return elem
        else:
            print("Erro! Pilha Vazia")

    def __repr__(self):
        r = ""
        pointer = self.first
        while(pointer):
            r = r + f'{pointer.data}' + " "
            pointer = pointer.next

    def __len__(self):
        return self._size

fila = Filaa()
fila.enfileira(1)
fila.enfileira(2)
fila.enfileira(3)
print(fila)














class Fila():
    def __init__(self):
        self._size = 0

        self.elementos = []
        self.frente = 0
        self.tras = self.frente
        self.maxtam = 3
        contador = self.maxtam
        while contador != 0:
            self.elementos += [None]
            contador -= 1
        print(self.elementos)
    def enfileira(self, elemento):
        if ((self.tras+1 % self.maxtam) == self.frente):
            print("Erro, a fila está cheia!")
        else:
            self.elementos = self.elementos[self.tras:self.tras] = [elemento]
            self.tras = (self.tras + 1) // self.maxtam

    def esvaziarFila(self):
        self.frente = 0
        self.tras = self.frente
        self.elementos = []

    def __len__(self):
        return self._size

    def isFilaVazia(self):
        return self.frente == self.tras

    def imprime(self):
        print("[", end="")
        contador = self.maxtam
        for elemento in self.elementos:
            if elemento == None:
                contador -= 1
                continue
            else:
                if contador != -1:
                    print(elemento, end=",")
                else:
                    print(elemento, end="")
            contador -= 1
        print("]")


#fila = Fila()
#fila.enfileira(1)
#fila.enfileira(2)
#fila.enfileira(3)
#fila.enfileira(4)
#fila.imprime()

