"""
Stwórz następujące funkcje. Niech każda z nich przyjmuje w argument do przeliczenia i zwraca przeliczoną wartość.

6. `pole_trojkata` - z trzema parametrami - oblicza pole trójkąta o podanych bokach z wzoru Herona.

Dla wybranych napisz też interaktywne programy, które pytają użytkownika o dane i wypisują wynik.

"""
bok_a = float(input('Podaj bok a trójkąta: '))
bok_b = float(input('Podaj bok b trójkąta: '))
bok_c = float(input('Podaj bok c trójkąta: '))

import math
def pole_trojkata (bok_a:float, bok_b:float,bok_c:float):
    """docstring: 3 argumenty, typ danych: float"""
    p = (bok_a + bok_b + bok_c) / 2
    if p * (p-bok_a) * (p-bok_b) * (p-bok_c) > 0:
        pole = math.sqrt(p * (p-bok_a) * (p-bok_b) * (p-bok_c))
    else:
        pole = 'Podane liczby nie stanowią trójkąta'
    return pole

print(f'Pole trójkąta = ',pole_trojkata(bok_a,bok_b,bok_c))

print(pole_trojkata.__doc__ )
print(60*'=')

def test_pole_trojkata_blad():
    assert pole_trojkata(1,1,5) == False

def test_pole_trojkata_ok():
    assert pole_trojkata(3,4,5 ) == 6