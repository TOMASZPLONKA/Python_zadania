"""
### Zadanie 2.4 | Zgadnij liczbę z zakresu
​
Program losuje liczbę z zakresu od 0 do 999. Użytkownik ma zgadnąć tę liczbę nie widząc jej.
Kiedy użytkownik poda nieprawidłowy wynik, program podpowiada pisząc czy podana liczba była za duża, czy za mała.
Gdy użytkownik poda właściwą liczbę, program wypisuje gratulacje jednocześnie informując, w której próbie udało się zgadnąć liczbę.
"""
import random
wylosowana_liczba = random.randint(0,999)
liczba_uzytkownika = int(input('Zgadnij wylosowaną liczbę: '))
licznik = 1
while wylosowana_liczba != liczba_uzytkownika:
    if liczba_uzytkownika < wylosowana_liczba:
        print('Szukana liczba jest większa od wprowadzonej liczby.')
    else:
        print('Szukana liczba jest mniejsza od wprowadzonej liczby.')
    liczba_uzytkownika = int(input('Zgadnij wylosowaną liczbę: '))
    licznik = licznik + 1
print(f'Gratulacje! Udało Ci się odgadnąć wylosowaną liczbę w {licznik} próbie.')


