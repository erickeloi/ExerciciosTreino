def lista_de_ocorrencias(lista_inteiros: list):
    elementos_unicos = []
    posicao_elementos_unicos = 0
    contador_ocorrencias = 0
    lista_de_ocorrencias = []
    posicao_lista_de_ocorrencias = 0

    for elemento in lista_inteiros:
        if elemento not in elementos_unicos:
            elementos_unicos += [elemento]
            posicao_elementos_unicos += 1
    
    for i in range(posicao_elementos_unicos):
        for numero in lista_inteiros:
            if numero == elementos_unicos[i]:
                contador_ocorrencias += 1
                ultimo_numero_aux = numero
        lista_de_ocorrencias = lista_de_ocorrencias + [f"{ultimo_numero_aux}:{contador_ocorrencias}"]
        contador_ocorrencias = 0
        posicao_lista_de_ocorrencias += 1
    
    return lista_de_ocorrencias

lista_teste = [1,2,2,2,2,2,2,1,3,3,3]
print(lista_de_ocorrencias(lista_teste))


#INACABADO
def maior_menor_ocorrencia(lista_inteiros):
    elementos_unicos = []
    lista_ocorrencias = []

    menor_ocorrencia = 0
    maior_ocorrencia = 0

    posicao_elementos_unicos = 0
    contador_ocorrencias = 0
    lista_de_ocorrencias = []
    posicao_lista_de_ocorrencias = 0

    lista_aux = []
    for elemento in lista_inteiros:
        if elemento not in elementos_unicos:
            elementos_unicos += [elemento]
            posicao_elementos_unicos += 1
    
    for i in range(posicao_elementos_unicos):
        for numero in lista_inteiros:
            if numero == elementos_unicos[i]:
                contador_ocorrencias += 1
                ultimo_numero_aux = numero
        

        lista_de_ocorrencias = lista_de_ocorrencias + [contador_ocorrencias]
        contador_ocorrencias = 0
        posicao_lista_de_ocorrencias += 1
    
    for i in range(posicao_lista_de_ocorrencias):
        posicao_maior = 0
        posicao_menor = 0
        
        if lista_de_ocorrencias[i] > maior_ocorrencia:
            maior_ocorrencia = lista_de_ocorrencias[i]
            posicao_maior = 0

        if lista_de_ocorrencias[i] < menor_ocorrencia:
            menor_ocorrencia = lista_de_ocorrencias[i]
            posicao_menor = 0
    

        return ""
    
        


