"""
# Zadanie 1
Napisz program obsługujący bazę danych pracowników.
W bazie danych przechowuj imię, nazwisko, email, rok urodzenia, pensję.Skorzystaj z modułu `json`.
Przykład użycia:$ python employees.py
Co chcesz zrobić? [d - dodaj, w - wypisz] d
Imie: Jan
Nazwisko: Nowak
Rok urodzenia: 1980
Pensja: 5000.0
$ python employees.py
Co chcesz zrobić? [d - dodaj, w - wypisz] w
Pracownicy:
- [1] Jan Nowak - rok: 1980, pensja: 5000.00 PLN
"""

import json

try:
    with open("pracownicy.json") as plik:
        pracownicy = json.load(plik)
except FileNotFoundError:
    pracownicy = [{"imie": "Jan", "nazwisko": "Nowak", "rok_urodzenia": 1980, "pensja": 5000.0}]

op = input("Co chcesz zrobić? [d - dodaj, w - wypisz]: ")
if op == "d":
    pracownik = {}
    pracownik['imie'] = input("Podaj imię: ")
    pracownik['nazwisko'] = input("Podaj nazwisko: ")
    pracownik['rok_urodzenia'] = input ("Podaj rok urodzenia: ")
    pracownik['pensja'] = input("Podaj pensję: ")
    pracownicy.append(pracownik)
    with open("pracownicy.json","w") as plik:
        json.dump(pracownicy,plik)
elif op == "w":
    for nr,p in enumerate(pracownicy,1):
        print(f"{nr} - {p['imie']} {p['nazwisko']}, {p['rok_urodzenia']}, {p['pensja']}")





