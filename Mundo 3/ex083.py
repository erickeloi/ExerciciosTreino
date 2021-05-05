# Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expressao = str(input("Digite uma expressão matemátiaca: ")).strip()
quantos_parenteses = expressao.count("(") + expressao.count(")")
if quantos_parenteses % 2 == 0:
    print("Expressão válida")
if quantos_parenteses % 2 == 1:
    print("Expressão inválida")
