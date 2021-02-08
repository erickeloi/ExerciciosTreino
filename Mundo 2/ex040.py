# Desafio 40
# Programa média escolar
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
if media >= 7:
    print(f"Parabéns, com sua média {media}, você foi Aprovado!")
elif 5.0 <= media <= 6.9:
    print(f"Atenção!!! Com a sua média {media} você está de Recuperação")
elif media < 5:
    print(f"Com a sua média {media}, você foi Reprovado.")
