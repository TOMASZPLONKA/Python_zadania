"""
Stwórz następujące funkcje. Niech każda z nich przyjmuje w argument do przeliczenia i zwraca przeliczoną wartość.

5. `bmi` - oblicza współczynnik BMI dla podanych dwóch parametrów: wzrostu w metrach i wagi w kg.

Dla wybranych napisz też interaktywne programy, które pytają użytkownika o dane i wypisują wynik.

"""

wzrost = int(input('Podaj wzrost (w cm): '))
waga = float(input('Podaj wagę (w kg): '))

def bmi(waga:float,wzrost:int):
    """docstring: składnia: waga, typ danych: int,
    wzrost, typ danych: float"""
    BMI = round((waga/(wzrost/100) ** 2),2)
    if BMI < 18.5:
        return print(f'Twoje BMI = {BMI}. Niedobrze. Masz niedowagę. Skontaktuj się z lekarzem i dietetykiem.')
    elif 18.5 <= BMI < 25:
        return print(f'Twoje BMI = {BMI}. Świetnie. Twoja waga jest w sam raz.')
    elif 25 <= BMI < 30:
        return print(f'Twoje BMI = {BMI}. Uważaj. Masz nadwagę.')
    else:
        return print(f'Twoje BMI = {BMI}. Jest bardzo źle! Chorujesz na otyłość. Natychmiast skonsultuj się z lekarzem.')

bmi(waga,wzrost)

print(bmi.__doc__ )
print(60*'=')

def test_BMI_Normal():
    assert BMI(87,187) == 24.88

def test_BMI_Nadwaga():
    assert BMI(110,200) == 27.5