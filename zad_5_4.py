"""
Zaimplementuj generatorzawierający listę wszystkich możliwych rozgrywek na podstawie dostarczonej listy graczy. Uwzględnij rewanże.
Przykładowe użycie:
for player_1, player_2 in tournament(['A','B','C']):
"""
def tournament(lista):
    for player_1 in lista:
        for player_2 in lista:
            if player_1 != player_2:
                yield player_1, player_2

# wszystkie pary bez rewanży

def tournament2(lista):
    for i1 in range(len(lista)):
        for i2 in range(i1 + 1,len(lista)):
            if i1 != i2:
                yield lista[i1],lista[i2]

for player_1, player_2 in tournament(['A','B','C']):
    print(player_1,player_2)

print(60*'-')

for player_1, player_2 in tournament2(['A','B','C']):
    print(player_1,player_2)
