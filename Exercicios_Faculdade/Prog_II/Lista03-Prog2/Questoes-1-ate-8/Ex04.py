class Histograma:
    def ler(self) -> None:
        caracteres = input("Digite sua série de caracteres: ").upper()
        self.caracteres = caracteres
        self.qntd_caracteres = len(caracteres)
        
    def mostra_histograma(self) -> None:
        frequencia_caracteres = {} 
        caracteres = self.caracteres 

        # Para mostrar o histograma em ordem alfabética, coloque a variavel ordenar como True
        ordenar: bool = False
        if ordenar:
            caracteres = sorted(caracteres)

        for i in caracteres: 
            if i in frequencia_caracteres: 
                frequencia_caracteres[i] += 1
            else: 
                frequencia_caracteres[i] = 1

        print (f"A Distribuição (Frequência) de letras é: {str(frequencia_caracteres)}")

hist = Histograma()
hist.ler()
hist.mostra_histograma()
