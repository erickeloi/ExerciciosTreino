class Contador:
    def inicializa(self):
        self.contagem: int = 0

    def incrementa(self):
        self.contagem += 1
    def decrementa(self):
        self.contagem -= 1
    
    # Extra
    def mostra_contagem(self):
        print(f"Contagem: {self.contagem}")

cont = Contador()
cont.inicializa()
cont.mostra_contagem()

cont.incrementa()
cont.incrementa()
cont.incrementa()
cont.incrementa()
cont.incrementa()

cont.mostra_contagem()

cont.decrementa()
cont.decrementa()
cont.decrementa()

cont.mostra_contagem()
