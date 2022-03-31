# TAD em python

class NumeroComplexo:
    def __init__(self, real: int, img: int): 
        self.real = real
        self.img = img

    def imprime(self): 
        print(f"{self.real} + {self.img}i")

    def copia(self, fonte, destino):
        aux = a
        a = b
        b = aux

    def soma(self, a, b):
        soma_real = a.real + b.real 
        soma_img = a.img + b.img
        return f"{soma_real} + {soma_img}i"

    def ehreal(self, teste):
        return bool(teste.img)

def main():
    a = NumeroComplexo(2,5)
    a.imprime()
    

if __name__ == "__main__":
    main()
