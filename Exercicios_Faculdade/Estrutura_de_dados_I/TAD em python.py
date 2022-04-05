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
    #TAD
    num_comp = str() 

    #INTERFACES
    def inicializa(real: float, img: float):
        num_comp_aux = NumeroComplexo()
        num_comp_aux.real = real
        num_comp_aux.img = img
        return num_comp_aux
        
    def imprime(num_comp_aux): 
        print(f"{num_comp_aux.real} + {num_comp_aux.img}i")

    def copia(fonte, destino):
        destino.real = fonte.real
        destino.img = fonte.img

    def soma(a, b):
        soma_real = a.real + b.real 
        soma_img = a.img + b.img
        return f"{soma_real} + {soma_img}i"

    def ehreal(teste):
        return bool(teste.img)

def main():
    a = NumeroComplexo.inicializa(2,5)
    print("Valor de a:")
    NumeroComplexo.imprime(a)
    
    b = NumeroComplexo.inicializa(5,10)
    print("Valor de b:")
    NumeroComplexo.imprime(b)
    print("Copiando o valor de 'a' para 'b'...")
    NumeroComplexo.copia(a,b)
    print("Novo valor de b:")
    NumeroComplexo.imprime(b)
    
    print("Somando valor de 'a' com 'b': ")
    soma = NumeroComplexo.soma(a,b)
    print(soma)
    
    teste_bool = NumeroComplexo.ehreal(a)
    print(teste_bool)
    
    
    

if __name__ == "__main__":
    main()
