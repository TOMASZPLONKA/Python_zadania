"""### Zadanie 1.3 | Współczynnik BMI (ok. 2 godz.)
​
Napisz trzy programy, które dla podanych liczb: wzrostu w cm i masy ciała w kg obliczą i wypiszą współczynnik BMI,
oraz podsumowanie informujące o stanie/zaleceniach. (Informacje o BMI: wzór, interpretację wyników, proszę znaleźć samodzielnie).
Programy mają różnić się sposobem interakcji z użytkownikiem."""

""" 
### BMI = masa/wzrost2
Wartość	
BMI < 18,5	niedowaga
18,5 ≤ BMI ≤ 24,9	waga prawidłowa
25 ≤ BMI ≤ 29,9	nadwaga
BMI > 30 otyłość"""

### I sposób
wzrost = int(input('Podaj wzrost (w cm): '))
waga = float(input('Podaj wagę (w kg): '))

BMI = round((waga/(wzrost/100) ** 2),2)

if BMI < 18.5:
    print(f'Twoje BMI = {BMI}. Niedobrze. Masz niedowagę. Skontaktuj się z lekarzem i dietetykiem.')
elif 18.5 <= BMI <= 24.9:
    print(f'Twoje BMI = {BMI}. Świetnie. Twoja waga jest w sam raz.')
elif 25 <= BMI <= 29.9:
    print(f'Twoje BMI = {BMI}. Uważaj. Masz nadwagę.')
else:
    print(f'Twoje BMI = {BMI}. Jest bardzo źle! Chorujesz na otyłość. Natychmiast skonsultuj się z lekarzem.')

print()

### II sposób

dane = list()
wzrost = int(input('Podaj wzrost (w cm): '))
dane.append(wzrost)
waga = float(input('Podaj wagę (w kg): '))
dane.append(waga)

print(dane)
BMI = round((dane[1] / (dane[0]/100) ** 2),2)

if BMI < 18.5:
    print(f'Twoje BMI = {BMI}. Niedobrze. Masz niedowagę. Skontaktuj się z lekarzem i dietetykiem.')
elif 18.5 <= BMI <= 24.9:
    print(f'Twoje BMI = {BMI}. Świetnie. Twoja waga jest w sam raz.')
elif 25 <= BMI <= 29.9:
    print(f'Twoje BMI = {BMI}. Uważaj. Masz nadwagę.')
else:
    print(f'Twoje BMI = {BMI}. Jest bardzo źle! Chorujesz na otyłość. Natychmiast skonsultuj się z lekarzem.')