"""
Stwórz następujące funkcje. Niech każda z nich przyjmuje w argument do przeliczenia i zwraca przeliczoną wartość.

3. `srednia` - oblicza średnią z dwóch liczb,

Dla wybranych napisz też interaktywne programy, które pytają użytkownika o dane i wypisują wynik.

"""

def average(liczba_a:float, liczba_b:float):
    """docstring: 2 argumenty, typ danych: float"""
    return (liczba_a + liczba_b)/2

print(average(15,-8.8))
print(average(2,2))
print(average(18,105))

print(average.__doc__ )
print(60*'=')

def test_average():
    assert average(12,15) == 13.5


#C:\Users\Ewa\workspace\projects\bootcamp\python20191116\3_funkcje
#zad_7.py
#C:\Users\Ewa\workspace\projects\bootcamp\Python_zadania\funkcje\zadania_domowe
#tp_zad_3.1c.py


