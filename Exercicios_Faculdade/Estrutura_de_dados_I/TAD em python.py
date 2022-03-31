# TAD em python

#Implemente um TAD Número Complexo
#   ¨cada número possui os campos real e imaginário¨

#   Implemente as operações:

#   Inicializa: atribui valores para os campos
#   Imprime: imprime o número da forma “R + Ci”
#   Copia: Copia o valor de um número para outro
#   Soma: Soma dois números complexos
#   EhReal: testa se um número é real

#   Faça um pequeno programa para testar o seu TAD

# TO-DO:
    # Fazer um arquivo separado para o TAD e Organizar melhor atributos e interfaces


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
