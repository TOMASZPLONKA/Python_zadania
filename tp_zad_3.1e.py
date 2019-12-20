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

bmi(87,187)


print(60*'=')

def test_BMI_Normal():
    assert bmi(87,187) == print(f'Twoje BMI = {24.88}. Świetnie. Twoja waga jest w sam raz.')

def test_BMI_Nadwaga():
    assert bmi(110,200) == print(f'Twoje BMI = {27.5}. Uważaj. Masz nadwagę.')
