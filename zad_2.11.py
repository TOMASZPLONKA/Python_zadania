"""
Napisz program zliczający liczbę unikalnych liczb wprowadzonych
przez użytkownika. Sprawdź jak dużo z tych liczb jest liczbami
parzystymi w zakresie 0-100 - w tym celu skorzystaj z operatora
iloczynu.
"""
# zbior = {} - to stworzy słownik, a nie zbiór

zbior = set(range(0,101,2))
"""
# inny sposób:
zbior = set()

for x in range(0,101,2):
    zbior.add(x)
print(zbior)
"""
liczby = set()
while True:
    liczba = (input('Podaj liczbę: '))
    if liczba == 'koniec':
        break
    else:
        liczby.add(int(liczba))
print(f'Unikalnych liczb: {len(liczby)}')
print(f'Wprowadzono następujące liczy parzyste w zakresie do 100: {zbior & liczby}')
print(f'Liczba wprowadzonych liczb parzystych w zakresie do 100: {len(zbior & liczby)}')
