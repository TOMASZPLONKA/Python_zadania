"""
# Zadanie 2Napisz program wczytujący plik z logami aktywności użytkowników w systemie. Na podstawie wczytanych danych wyświetl informację o sumarycznym czasie przebywania każdego użytkownika w systemie.Przykład użycia:$ python read_logs.py logs.txt
Czas przebywania w systemie:
- user-1: 92 s
- user-2: 51 s
- user-3: 20 s

"""
with open("logs.txt") as plik:
    wiersze = plik.read().split("\n")

login = {}
logout = {}
for wiersz in wiersze:
    lista = wiersz.split(";")
    kto = lista[0]
    operacja = lista[1]
    czas = int(lista[2])
    if operacja =='LOGIN':
        if kto not in login:
            login[kto] = 0
        login[kto] += czas
    elif operacja =='LOGOUT':
        if kto not in logout:
            logout[kto] = 0
        logout[kto] += czas

czas_w_systemie = {u: logout[u]-login[u] for u in logout}
for k, v in sorted(czas_w_systemie.items(),key = lambda x: x[1]):
    print(f'{k}, czas: {v}')









