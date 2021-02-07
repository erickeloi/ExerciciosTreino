#Programa analisador
#Dado um certo tipo de informação, o programa analisa e mostra na tela algumas informações sobre ela.
dado = input("Digite aqui uma informação para ela ser analisada: ")
print(f'O tipo primitivo Dessa informação é: {type(dado)}')
print("A informação é Numerico? {}".format(dado.isnumeric()))
print("A informação é Alfabetico? {}".format(dado.isalpha()))
print("A informação é Capitalizada? {}".format(dado.istitle()))
#Percebi agora que a partir do python 3.7 dá pra formatar sem o .format, só colocar o f e dentro do placeholder o onjeto/metodo etc
