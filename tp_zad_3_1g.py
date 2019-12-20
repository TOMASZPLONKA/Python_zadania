"""
Stwórz następujące funkcje. Niech każda z nich przyjmuje w argument do przeliczenia i zwraca przeliczoną wartość.

7. `kilometry_na_mile` - przelicza odległość wyrażoną w kilometrach na mile

Dla wybranych napisz też interaktywne programy, które pytają użytkownika o dane i wypisują wynik.

"""
def kilometry_na_mile(odleglosc_km:float):
    """docstring: wprowadzona odległość podana w kilometrach, typ danych: float"""
    odleglosc_mile = odleglosc_km / 1.609
    return odleglosc_mile

print(kilometry_na_mile(5))
print(kilometry_na_mile(12))

print(kilometry_na_mile.__doc__ )
print(60*'=')

def test_kilometry_na_mile():
    assert kilometry_na_mile(15) == 9.322560596643878