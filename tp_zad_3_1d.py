"""
Stwórz następujące funkcje. Niech każda z nich przyjmuje w argument do przeliczenia i zwraca przeliczoną wartość.

4. `pole_kola` - oblicza pole koła o podanym promieniu (jeden parametr)
podpowiedź: wartość PI jest dostępna jako `Math.PI`

Dla wybranych napisz też interaktywne programy, które pytają użytkownika o dane i wypisują wynik.

"""

import math
r = float(input('Podaj promień koła: '))
def pole_kola(r):
    """docstring: 1 argument - promień koła, typ danych: float"""
    return math.pi * r**2
print(f'Pole koła o promieniu {r} = ',pole_kola(r))

print(pole_kola.__doc__ )
print(60*'=')

def test_pole_kola():
    assert pole_kola(2) == 12.566370614359172