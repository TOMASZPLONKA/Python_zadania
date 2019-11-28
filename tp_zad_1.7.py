"""
### Zadanie 1.7 | Liczenie cen (ok. 0,5 godz.)
​
Przy pomocy `input()` zapytaj użytkownika co chce kupić, jaką ilość towaru chce kupić i jaka jest jego cena.
Wyświetl odpowiedni komunikat.
​
Przykład:
Co chcesz kupić? - ziemniaki
Podaj cenę towaru - 5
Podaj ilość towaru - 10
​
Za ziemniaki, który chcesz kupić, zapłacisz 50 zł
"""
produkt = input('Co chesz kupić? ')
cena = float(input('Podaj cenę towaru: '))
ilosc = float(input('Podaj ilość towaru: '))
koszt = cena * ilosc

print(f'Za {produkt} zapłacisz {koszt:.2f} zł.')

