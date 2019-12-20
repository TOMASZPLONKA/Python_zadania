"""
Stwórz następujące funkcje. Niech każda z nich przyjmuje w argument do przeliczenia i zwraca przeliczoną wartość.

2. `max` - zwraca większą z dwóch liczb,

Dla wybranych napisz też interaktywne programy, które pytają użytkownika o dane i wypisują wynik.

"""

def max(liczba_a:float, liczba_b:float):
    """docstring: 2 argumenty, typ danych: float"""
    if liczba_a >= liczba_b:
        return liczba_a
    else:
        return liczba_b

print(max(15,-8.8))
print(max(2,2))
print(max(18,105))

print(max.__doc__ )
print(60*'=')

def test_max2():
    assert max(12,15) == 15

def test_max1():
    assert max(20,8) == 20

def test_max1_2():
    assert max(16,16) == 16