# TO-DO: Melhorar, elaborar e fazer um TAD

# print(ord('a')) # ASCII to Decimal  

# print(chr(97)) # Decimal to ASCII

# 1. identificar maiusculo com a tabela ascii
# 65 até 90
# 2. identificar minusculo com a tabela ascii
# 97 até 122

# 1.
def eh_maiusculo(digito: str):
    if digito.isnumeric():
        if 65 <= int(digito) <= 90:
            return 1
        else:
            return 0
    else:
        if digito.isalpha():
            if 65 <= ord(digito) <= 90:
                return 1
            else:
                return 0

def eh_minusculo(digito: str):
    if digito.isnumeric():
        if 97 <= int(digito) <= 122:
            return 1
        else:
            return 0
    elif digito.isalpha():
        if 97 <= ord(digito) <= 122:
            return 1
        else:
            return 0

def converter(digito: str):
    if eh_maiusculo(digito):
        digito = chr(ord(digito) + 32)
        return digito
    elif eh_minusculo(digito):
        digito = chr(ord(digito) - 32)
        return digito


a = str(input("Digite um caracter ou o decimal dele: "))
print("Ele é Minusculo?")
print(bool(eh_minusculo(a)))

print("Convertendo...")
print(converter(a))
