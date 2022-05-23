#import pandas as pd
import re
import string
import matplotlib.pyplot as plt

#texto1 = open("texto5.txt", "r", encoding="utf8").read()
texto2 = open("texto37.txt", "r", encoding="utf8").read()
stopwords = open("stopwords2.txt", "r", encoding="utf8").read().split("\n")

texto2 = texto2.lower()
texto2 = texto2.translate(str.maketrans("","", string.punctuation))
texto2 = texto2.replace("‘","")
texto2 = texto2.replace("’","")
texto2 = texto2.split(" ")

clean_text = []
for word in texto2:
    if word not in stopwords:
        clean_text.append(word)

word_count = []
palavras_unicas = []
ocorrencias_unicas = []
#contador = []
for word in clean_text:
    if word not in palavras_unicas:
        aux = {
            f'word': word,
            'ocorrencies': clean_text.count(word)
        }
        word_count.append(aux)
        palavras_unicas.append(word)
        ocorrencias_unicas.append(clean_text.count(word))
        #contador.append(clean_text.count(word))

  
        
word_count = sorted(word_count, key= lambda x: x['ocorrencies'], reverse=True)


#print(word_count)
contador = 0
#while contador < 10:
#    for single_dict in word_count:
#        for value in single_dict.values():
#            print(value, end = " ")
#            contador += 1
#            if contador % 2 == 0:
#                print()

lista_palavra_freq = []
for c in range(10):
    lista_palavra_freq.append(f"{word_count[c]}:{word_count[c]}")

#print(lista_palavra_freq)

#word_count.plot(30,title='Frequency distribution for 30 most common tokens in our text collection')

print(palavras_unicas[:10])
print(ocorrencias_unicas[:10])

plt.bar(range(len(palavras_unicas[:10])), ocorrencias_unicas[:10])

plt.title("Palavras mais frequentes")
plt.ylabel("Num. de palavras unicas")

plt.xticks(range(len(ocorrencias_unicas[:10])), ocorrencias_unicas[:10])
plt.show()

#plt.bar(a, b)

#plt.title("Palavras mais frequentes")
#plt.ylabel("Num. de palavras unicas")

#plt.xticks(a, b)
#plt.show()
