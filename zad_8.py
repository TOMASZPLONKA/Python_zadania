napis = input("Podaj napis: ")

if napis.count('<') != 1 or napis.count('>') != 1:
    print('Zła liczba nawiasów!')
    exit() # uruchomienie exit powoduje natychmiastowe zatrzymanie programu

czy_zliczac = False
ile_znakow = 0

for znak in napis:
    if znak == '<':
         czy_zliczac = True
    elif znak == '>':
         czy_zliczac = False
    elif czy_zliczac == True:
        ile_znakow += 1

print(f'Liczba znaków pomiędzy znakami "<" i ">": {ile_znakow} ')