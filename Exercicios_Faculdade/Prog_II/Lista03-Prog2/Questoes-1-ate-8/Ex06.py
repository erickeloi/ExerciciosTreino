class NumeroComplexo:
    def inicializaNumero(self, real: float, img: float):
        self.real = real
        self.img = img

    def ImprimeNumero(self): 
        print(f"{self.real} + {self.img}i")
    
    def eIgual(self, numC):
        if ((self.real == numC.real) and (self.img == numC.img)):
            return True
        else:
            return False

    def soma(self, numC):
        self.real += numC.real
        self.img += numC.img

    def subtrai(self, numC):
        self.real -= numC.real
        self.img -= numC.img

    def multiplica(self, numC):
        a = self.real
        b = self.img

        c = numC.real
        d = numC.img

        parte_real = a*c - b*d
        parte_imaginaria =  a*d + b*c

        self.real = parte_real
        self.img = parte_imaginaria

    def divide(self, numC):
        a = self.real
        b = self.img

        c = numC.real
        d = numC.img

        parte_real = ((a*c+b*d)/(c**2+d**2))
        parte_imaginaria = ((b*c-a*d)/(c**2+d**2))

        self.real = parte_real
        self.img = parte_imaginaria

# Testes
print("mostrando n1")
n1 = NumeroComplexo()
n1.inicializaNumero(1,2)
n1.ImprimeNumero()

print("mostrando n2")
n2 = NumeroComplexo()
n2.inicializaNumero(3,4)
n2.ImprimeNumero()

print("Somando n1 + n2")
n1.soma(n2)
n1.ImprimeNumero()

print("Subtraindo n1 - n2")
n1.subtrai(n2)
n1.ImprimeNumero()

print("Multiplicando n1 * n2")
n1.multiplica(n2)
n1.ImprimeNumero()

print("Resetando n1...")
n1 = NumeroComplexo()
n1.inicializaNumero(1,2)
n1.ImprimeNumero()

print("Divide n1 / n2")
n1.divide(n2)
n1.ImprimeNumero()
