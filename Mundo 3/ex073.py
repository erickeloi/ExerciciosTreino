# Desafio 73
# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética. 
# d) Em que posição está o time da Chapecoense.
brasileirao = ('Flamengo', 'Internacional', 'Atletico-MG', 'São Paulo', 'Fluminense', 'Grêmio', 'Palmeiras', 'Santos', 'Athletico-PR', 'Corinthians', 'Bragantino', 'Ceará', 'Atlético-GO', 'Sport', 'Bahia', 'Fortaleza', 'Vasco', 'Goiás', 'Coritiba', 'Botafogo')
print(f'Os 5 primeiros colocados são: {brasileirao[0:5]}')
print(f"Os 4 últimos colocados da tabela são: {brasileirao[-4:]}")
print(f"Os times em ordem alfabética:\n {sorted(brasileirao)}")
if 'Chapecoense' in brasileirao:
    print(f"A Chapecoense está na posição: {brasileirao.index('Chapecoense') + 1}")
else:
    print(f"Posição em que está o time da chapecoense: Não está na serie A (23 / 02 / 2021) ")
