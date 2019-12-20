"""
### Zadanie 3.2 | Miesiące
​
Zapytaj użytkownika o nazwę miesiąca i na tej podstawie wypisz mu ile dni na dany miesiąc.
​
Logikę obliczania liczby dni wydziel do osobnej funkcji.
​
**Wersja A**
Nie przyjmuj się lutym - zwracaj zawsze jedną wartość.
​
**Wersja B (trudniejsza)**
Jeżeli użytkownik poda luty - zapytaj go o rok. Na tej podstawie policz czy w tym roku luty był przestępny czy nie.
​

"""
# WERSJA B

miesiac = input("Podaj nazwę miesiąca: ")
miesiace = {
    'styczeń':31,
    'luty':28,
    'luty_p':29,
    'marzec':31,
    'kwiecień':30,
    'maj':31,
    'czerwiec':30,
    'lipiec':31,
    'sierpień':31,
    'wrzesień':30,
    'październik':31,
    'listopad':30,
    'grudzień':31
}

import time
localtime = time.localtime(time.time())

def month (miesiac:str,rok = localtime.tm_year):
    if miesiac == 'luty':
        rok = int(input("Podaj rok: "))
        if rok % 4 == 0 and (rok % 400 != 100 and rok % 400 != 200 and rok % 400 != 300):
            print(miesiac, 'w',rok, 'roku ma', miesiace['luty_p'], 'dni')
        else:
            print(miesiac, 'w',rok, 'roku ma', miesiace[miesiac], 'dni')
    else:
        if miesiac in miesiace.keys():
            print(miesiac,'ma', miesiace[miesiac],'dni')

month(miesiac)

import pytest
def test_month_luty_niepodzielne_przez_400():
    assert month('luty',1900) == 28

def test_month_luty_przestepne():
    assert month('luty',2016) == 29
    
def test_month():
    assert month('czerwiec') == 30
