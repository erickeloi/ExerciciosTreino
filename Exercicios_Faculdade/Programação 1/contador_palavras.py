import re
import string

# ALUNO: ERICK ELOI PIMENTA PIMENTEL
# MATRICULA: 202111140012

# Modifique o nome dos blocos de texto para 'texto1' e 'texto2' para o programa funcionar !!!
texto1 = open("texto1.txt", "r", encoding="utf8").read()
texto2 = open("texto2.txt", "r", encoding="utf8").read()

def sanitize_text(text):
    texto2 = text
    texto2 = texto2.strip()
    texto2 = texto2.lower()
    texto2 = texto2.translate(str.maketrans("","", string.punctuation))
    texto2 = texto2.replace("‘","")
    texto2 = texto2.replace("’","")
    texto2 = texto2.split("\n")
    texto2 = " ".join(texto2)
    return texto2

texto1 = sanitize_text(texto1)
texto2 = sanitize_text(texto2)

texto1 = texto1.split(" ")
texto2 = texto2.split(" ")

word_count_1 = []
palavras_unicas_1 = []
ocorrencias_unicas_1 = []

for word in texto1:
    if word not in palavras_unicas_1:
        if word == "" or word == " ":
            continue
        aux = {
            f'word': word,
            'ocorrencies': texto1.count(word)
        }
        word_count_1.append(aux)
        palavras_unicas_1.append(word)
        ocorrencias_unicas_1.append(texto1.count(word))
        #contador.append(clean_text.count(word))

word_count_1 = sorted(word_count_1, key= lambda x: x['ocorrencies'], reverse=True)

#print(word_count_1)

word_count_2 = []
palavras_unicas_2 = []
ocorrencias_unicas_2 = []

for word in texto2:
    if word not in palavras_unicas_2:
        if word == "" or word == " ":
            continue
        aux = {
            f'word': word,
            'ocorrencies': texto2.count(word)
        }
        word_count_2.append(aux)
        palavras_unicas_2.append(word)
        ocorrencias_unicas_2.append(texto1.count(word))
        #contador.append(clean_text.count(word))

word_count_2 = sorted(word_count_2, key= lambda x: x['ocorrencies'], reverse=True)

#print(word_count_2)
def pegar_menor_ocorrencia(dict_word1, dict_word2):
    contador_inicial = 0
    contador_menor_ocorrencia_1 = 0
    palavra_com_menor_ocorrencia_t1 = ""
    for dado in word_count_1:
        if contador_inicial == 0:
            contador_menor_ocorrencia_1 = dado['ocorrencies']
            palavra_com_menor_ocorrencia_t1 = dado['word']
            contador_inicial += 1
        else:
            if dado['ocorrencies'] < contador_menor_ocorrencia_1:
                contador_menor_ocorrencia_1 = dado['ocorrencies']
                palavra_com_menor_ocorrencia_t1 = dado['word']
            
            contador_inicial += 1

    #print(palavra_com_menor_ocorrencia_t1)
    #print(contador_menor_ocorrencia_1)

info_final = []
for uniq_word1 in word_count_1:
    for uniq_word2 in word_count_2:
        if uniq_word1['word'] == uniq_word2['word']:
            if uniq_word1['ocorrencies'] > uniq_word2['ocorrencies']:
                dado = {'word': f'{word}',
                        'ocorrencia': f"{uniq_word2['ocorrencies']}"}
                info_final.append(dado)

            else:
                dado = {'word': f'{word}',
                        'ocorrencia': f"{uniq_word1['ocorrencies']}"}
                info_final.append(dado)

print("Dicionario de palavras que se repetiram em comum: ")
print(info_final)

print("Palavra que mais se repetiu em comum: ")

palavra_final = sorted(info_final, key=lambda x: x['ocorrencia'], reverse=True)
print(f"Palavra: {palavra_final[0]['word']}, Ocorrencias: {palavra_final[0]['ocorrencia']}")
