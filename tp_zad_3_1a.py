"""
Stwórz następujące funkcje. Niech każda z nich przyjmuje w argument do przeliczenia i zwraca przeliczoną wartość.
​
1. `stopy_na_metry` - przelicza odległość wyrażoną w stopach na metry,

Dla wybranych napisz też interaktywne programy, które pytają użytkownika o dane i wypisują wynik.

"""

def stopy_na_metry(odleglosc_foot:float):
    """docstring: wprowadzona odległość podana w stopach, typ danych: float"""
    odleglosc_metr = odleglosc_foot * 0.3048
    return odleglosc_metr

print(stopy_na_metry(3))
print(stopy_na_metry(10))
zmienna = float(input('Podaj odległość (w stopach):'))

print(f'{zmienna} stóp = ', stopy_na_metry(zmienna),' metrów')

print(stopy_na_metry.__doc__ )
print(60*'=')

def test_stopy_na_metry():
    assert stopy_na_metry(15) == 4.572







