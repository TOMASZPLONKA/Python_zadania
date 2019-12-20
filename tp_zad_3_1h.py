"""
Stwórz następujące funkcje. Niech każda z nich przyjmuje w argument do przeliczenia i zwraca przeliczoną wartość.

8. `mile_na_kilometry` - przelicza odległość wyrażoną w milach na kilometry

Dla wybranych napisz też interaktywne programy, które pytają użytkownika o dane i wypisują wynik.

"""

def mile_na_kilometry(odleglosc_mile:float):
    """docstring: wprowadzona odległość podana w milach, typ danych: float"""
    odleglosc_km = odleglosc_mile * 1.609
    return odleglosc_km

print(mile_na_kilometry(3))
print(mile_na_kilometry(15))

dana = float(input('Podaj odległość (w milach): '))
print(f'{dana} mil =', mile_na_kilometry(dana),' kilometrów')


print(mile_na_kilometry.__doc__ )
print(60*'=')

def test_mile_na_kilometry():
    assert mile_na_kilometry(10) == 16.09