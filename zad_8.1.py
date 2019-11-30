napis = input("Podaj napis: ")

if napis.count('<') != 1 or napis.count('>') != 1:
    print('Zła liczba nawiasów!')
    exit() # uruchomienie exit powoduje natychmiastowe zatrzymanie programu
liczba_znakow = napis.index('>') - napis.index('<') - 1

print(f'Liczba znaków pomiędzy znakami "<" i ">": {liczba_znakow} ')


napis = input("Podaj napis: ")

if napis.count('<') != 1 or napis.count('>') != 1:
    print('Zła liczba nawiasów!')
    exit() # uruchomienie exit powoduje natychmiastowe zatrzymanie programu
liczba_znakow = len( napis[ napis.index('<') + 1 : napis.index('>') ] )

print(f'Liczba znaków pomiędzy znakami "<" i ">": {liczba_znakow} ')