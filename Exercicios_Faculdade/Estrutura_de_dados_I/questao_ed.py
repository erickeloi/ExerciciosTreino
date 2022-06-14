from re import I


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
        
        print("Sites cadastrados: ")
        r = ""
        pointer = self.first
        while(pointer):
            r = r + f'{pointer.data[0]}' + ", "
            pointer = pointer.next
        print(r)
    
    

    def busca_site(self, nome: str):
        """Função que busca um site na fila, e se achar, move o Nó para o inicio da fila"""
        contador = 0

        pointer = self.first
        pointer_last = self.first
        while pointer != None:
            if contador > 0:
                pointer_last = pointer_last.next

            if pointer.data[0] == nome:
                print("Site encontrado!")
                print(f"link: {pointer.data[1]}")

                aux = pointer.data
                pointer_last.next = pointer.next
                return None
            else:
                pointer = pointer.next
                contador += 1
        print("Site não encontrado! \ Site não cadastrado!")

    def busca_site_aux(self, nome: str):
        index, ponteiro = self._index(nome)
        if index == None:
            print("Elemento não encontrado")
            
        elif index == 0:
            print("Site encontrado!")
            print(f"Link: {ponteiro.data[1]}")
        elif index == self._size:
            
            c = 0
            pointeiro_aux = self.first

            while c < self._size - 1:
                c += 1
                pointeiro_aux = pointeiro_aux.next
            # Penultimo elemento = ponteiro_aux
            # O penultimo elemento passa a ser o ultimo
            pointeiro_aux.next = None
            self.last = pointeiro_aux

            self.fura_fila(ponteiro.data[0], ponteiro.data[1])

    def _index(self, nome: str):
        """Dado um nome, procura e retorna em qual index esse nome está alocado"""
        pointer = self.first
        contador = 0
        while pointer:
            if pointer.data[0] == nome:
                return contador, pointer
            else:
                pointer = pointer.next
                contador += contador

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

bd.mostra_fila()

bd.busca_site_aux("pudim")

bd.mostra_fila()
