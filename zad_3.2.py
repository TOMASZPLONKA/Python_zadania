"""
Napisz funkcję zwracającą zbiór wszystkich znaków występujących w
napisie więcej niż zadana liczba razy.
Przykład użycia:
wiecej_niz('ala ma kota a kot ma ale', 3)
{'a', ' '}
"""

"""
I WERSJA
def wiecej_niz(napis, ile_znakow):
    wystapienia = dict()
    for litera in napis:
        if litera in wystapienia:
            wystapienia[litera] +=1
        else:
            wystapienia[litera] =1
    wynik = set()
    for litera,liczba_wystapien in wystapienia.items():
        if liczba_wystapien > ile_znakow:
            wynik.add(litera)
    return wynik
"""
"""
II WERSJA
def wiecej_niz(napis,ile_znakow):
    wynik = set()
    for znak in napis:
        if napis.count(znak) > ile_znakow:
            wynik.add(znak)
    return wynik """

# III WERSJA # set comprehension
def wiecej_niz(napis,ile_znakow):
    return {znak for znak in napis if napis.count(znak) > ile_znakow}

def test_dla_pustego_napisu():
    assert wiecej_niz('',3) == set()

def test_dla_niepustego_napisu():
    assert wiecej_niz('aaaaabbbccd',2) == {'a','b'}

