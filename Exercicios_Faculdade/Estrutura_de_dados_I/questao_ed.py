
class Node():
    """ Nós, que vão encadear a fila"""
    def __init__(self, nome: str, link:str):
        self.data = [nome, link]
        self.next = None

class Fila():
    """ Estrutura de dados 'FILA'/'QUEUE' """
    def __init__(self):
        self._size = 0

        self.first = None
        self.last = self.first
    
    def insere_site(self, nome: str, link: str):
        """ Basicamente função 'PUSH', insere um elemento no fim da fila"""
        node = Node(nome, link)

        if self.last == None:
            self.last = node
        else:
            self.last.next = node
            self.last = node
            
        if self.first == None:
            self.first = node

        self._size += 1

    def retira_primeiro_site(self):
        """ Basicamente função 'POP', tira o elemento do começo da fila"""
        if self.first != None:
            elem = self.first.data 
            self.first = self.first.next
            self._size -= 1
            return elem
        else:
            print("Erro! Pilha Vazia")


    def fura_fila(self, nome: str, link: str):
        """ Insere um elemento no começo da fila """
        node = Node(nome, link)

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

    def mostra_fila_debug(self):
        """ Mostra toda a pilha sem formatação ao usuário, Basicamente a função Print """
        r = ""
        pointer = self.first
        while(pointer):
            r = r + "" + f'{pointer.data}' + " , "
            pointer = pointer.next
        print(r)
    
    def mostra_fila(self):
        """ Mostra a pilha formatada ao usuário, Basicamente a função Print """
        print("Mostrando sites cadastrados... ")
        r = ""
        pointer = self.first
        while(pointer):
            r = r + f'{pointer.data[0]}' + ", "
            pointer = pointer.next
        print(r)

    def busca_site(self, nome: str):
        index, ponteiro = self._index(nome)
        if index == None:
            print("Elemento não encontrado")
        elif index == 0:
            print("Site encontrado!")
            print(f"Link: {ponteiro.data[1]}")
        elif index < self._size:
            print("Site encontrado!")
            print(f"Link: {ponteiro.data[1]}")
            c = 0

            pointeiro_aux = self.first
            while c < index - 1:
                c += 1
                pointeiro_aux = pointeiro_aux.next
            # elemento anterior ao desejado = ponteiro_aux
            data_aux = pointeiro_aux.next.data
            pointeiro_aux.next = pointeiro_aux.next.next

            self.fura_fila(data_aux[0], data_aux[1])
        elif index == self._size:
            print("Site encontrado!")
            print(f"Link: {ponteiro.data[1]}")
            c = 0

            pointeiro_aux = self.first
            while c < index - 1:
                c += 1
                pointeiro_aux = pointeiro_aux.next
            # elemento anterior ao desejado = ponteiro_aux
            data_aux = pointeiro_aux.next.data
            pointeiro_aux.next = None
            pointeiro_aux = self.last
            self.fura_fila(data_aux[0], data_aux[1])


    def _index(self, nome: str):
        """Dado um nome, procura e retorna em qual index esse nome está alocado"""
        pointer = self.first
        
        contador = 0
        while pointer:
            if pointer.data[0] == nome:
                return contador, pointer
            else:
                pointer = pointer.next
                contador += 1

        print("Elemento não encontrado na lista!")
        return None, None

    def __len__(self):
        """ Mostra o tamanho da fila ao usar a função len() na fila """
        return self._size

bd = Fila()
bd.insere_site("facebook", "https://www.facebook.com")
bd.insere_site("instagram", "https://www.instagram.com")
bd.insere_site("twitter", "https://twitter.com")
bd.insere_site("netflix", "https://www.netflix.com/")
bd.insere_site("amazon", "https://www.amazon.com.br")
bd.insere_site("pudim", "http://www.pudim.com.br")

print("Mostrando a o banco de dados (fila)...")
bd.mostra_fila()

print("---")
print("Buscando por Pudim...")
bd.busca_site("pudim")
print("---")
bd.mostra_fila()

print("---")
print("Buscando por Twitter...")
bd.busca_site("twitter")
print("---")

bd.mostra_fila()

print("---")
print("Buscando por Amazon...")
bd.busca_site("amazon")
print("---")

bd.mostra_fila()
