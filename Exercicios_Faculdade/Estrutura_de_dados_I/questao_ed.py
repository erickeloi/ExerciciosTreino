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


    def fura_fila(self, nome: str, link: str, aumentar_tamanho: bool = False):
        """ Insere um elemento no começo da fila """
        node = Node(nome, link)

        aux_pointer = self.first
        self.first = node
        self.first.next = aux_pointer
        if aumentar_tamanho:
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
        ponteiro = self.first
        ponteiro_ant = None
        contador = 0
        while ponteiro:
            if ponteiro.data[0] == nome:
                break
            else:
                contador += 1
                ponteiro_ant = ponteiro
                ponteiro = ponteiro.next
        if contador == 0:
            print("Site encontrado!")
            print(f"Link: {ponteiro.data[1]}")
        elif contador < self._size:
            print("Site encontrado!")
            print(f"Link: {ponteiro.data[1]}")
            # elemento anterior ao desejado = ponteiro_aux
            data_aux = ponteiro.data
            ponteiro_ant.next = ponteiro.next

            self.fura_fila(data_aux[0], data_aux[1])
        elif contador == self._size:
            print("Site encontrado!")
            print(f"Link: {ponteiro.data[1]}")

            # elemento anterior ao desejado = ponteiro_aux
            data_aux = ponteiro.data
            ponteiro_ant.next = None
            self.last = ponteiro_ant
            self.fura_fila(data_aux[0], data_aux[1])
        else:
            print("Elemento não encontrado")

    def _index(self, nome: str):
        """Dado um nome, procura e retorna em qual index esse nome está alocado, também retorna o ponteiro e o ponteiro do antecessor"""
        pointer = self.first
        pointer_ant = None
        contador = 0
        while pointer:
            if pointer.data[0] == nome:
                return contador, pointer, pointer_ant
            else:
                contador += 1
                pointer_ant = pointer
                pointer = pointer.next
                


    def remove_site(self, nome: str):
        ponteiro = self.first
        ponteiro_ant = None

        contador = 0
        while ponteiro:
            if ponteiro.data[0] == nome:
                break
            else:
                contador += 1
                if contador == self._size:
                    contador = -1
                    break
                ponteiro_ant = ponteiro
                ponteiro = ponteiro.next

        if contador == -1:
            print("Elemento não encontrado")
        elif contador == 0:
            print(f"Removendo o site {ponteiro.data[0]}...")
            self.first = self.first.next
            self._size -= 1
        elif contador < self._size:
            print(f"Removendo o site {ponteiro.data[0]}...")
            # elemento anterior ao desejado = ponteiro_aux
            ponteiro_ant.next = ponteiro.next
            self._size -= 1
        elif contador == self._size:
            print(f"Removendo o site {ponteiro.data[0]}...")

            # elemento anterior ao desejado = ponteiro_aux
            ponteiro_ant.next = None
            self.last = ponteiro_ant
            self._size -= 1
        else:
            print("Elemento não encontrado na lista!")

    def __len__(self):
        """ Mostra o tamanho da fila ao usar a função len() na fila """
        return self._size

def quebra_linha():
    print("---")
    print("\n")
bd = Fila()
bd.insere_site("facebook", "https://www.facebook.com")
bd.insere_site("instagram", "https://www.instagram.com")
bd.insere_site("twitter", "https://twitter.com")
bd.insere_site("netflix", "https://www.netflix.com/")
bd.insere_site("amazon", "https://www.amazon.com.br")
bd.insere_site("pudim", "http://www.pudim.com.br")

print("Mostrando o banco de dados (fila)...")
bd.mostra_fila()
quebra_linha()

print("Buscando por Pudim...")
bd.busca_site("pudim")
quebra_linha()

bd.mostra_fila()
quebra_linha()

print("Buscando por Twitter...")
bd.busca_site("twitter")
quebra_linha()

bd.mostra_fila()
quebra_linha()

print("Buscando por Amazon...")
bd.busca_site("amazon")
quebra_linha()

bd.mostra_fila()
quebra_linha()

print(" Removendo o site Twitter ")
bd.remove_site("twitter")

bd.mostra_fila()
quebra_linha()

print(" Tentando Remover o site Twitter novamente (ele não está mais no banco de dados )")
bd.remove_site("twitter")
quebra_linha()

bd.mostra_fila()
quebra_linha()
