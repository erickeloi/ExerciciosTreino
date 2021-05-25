# Exercício Python 114: Site está acessível?
# Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br')
except:
    print("O site 'pudim.com.br' não está acessivel no momento")
else:
    print("O site 'pudim.com.br' está acessivel")
