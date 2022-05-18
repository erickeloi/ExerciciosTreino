#import pandas as pd

#texto1 = open("texto5.txt", "r", encoding="utf8").read()
texto2 = open("texto37.txt", "r", encoding="utf8").read()
stopwords = open("stopwords2.txt", "r", encoding="utf8").read().split("\n")

texto2 = texto2.lower().split()

clean_text = []
for word in texto2:
    if word not in stopwords:
        clean_text.append(word)

word_count = []
palavras_unicas = []
#contador = []
for word in clean_text:
    if word not in palavras_unicas:
        aux = {
            'word': word,
            'ocorrencies': clean_text.count(word)
        }
        word_count.append(aux)
        palavras_unicas.append(word)
        #contador.append(clean_text.count(word))

  
        
word_count = sorted(word_count, key= lambda x: x['ocorrencies'], reverse=True)


#print(word_count)
contador = 0
while contador < 10:
    for single_dict in word_count:
        for value in single_dict.values():
            print(value)
            contador += 1