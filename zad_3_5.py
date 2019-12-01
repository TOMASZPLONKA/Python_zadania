""""
Zaimplementuj funkcję obliczającą silnie dla zadanej wartości.
Przykład użycia:
silnia(5)
120
"""
def silnia(n:int):
    if n < 0 or type(n) is not int:
        #return None  mankament tego rozwiązania - programista używający tej funkcji będzie musiał sprawdzić czy nie dostał wartości None
        raise ValueError('n musi być intem i być większe lub równe 0')

    wynik = 1
    for i in range (1,n+1):
        wynik = wynik*i
    return wynik
print(silnia(4))

import pytest
def test_n_mniejsze_od_zera():
    with pytest.raises(ValueError):
        silnia(-10)
def test_n_zero():
    assert silnia (0) == 1

def test_n_wieksze_od_0():
    assert silnia(3) == 6
    assert silnia(4) == 24
    assert silnia(5) == 120
    assert silnia(6) == 720
    assert silnia(7) == 5040
