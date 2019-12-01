"""
Napisz program wyliczający kwotę należną za zakupiony towar na
podstawie podanej przez użytkownika wagi i nazwy produktu. Do
przechowywania informacji o cenie za kilogram danego produktu
użyj słownika. Wypisz wszystkie dostępne produkty w sklepie.
"""

produkty = {
    'ziemniaki' : 2.00,
    'pomidory' : 8.50,
    'jabłka' : 2.99,
}

print('Dostępne produkty w sklepie:')
for produkt, cena_za_kg in produkty.items():
    print(f'{produkt} - {cena_za_kg:.2f} zł/kg')

co = input('Co chcesz kupić z powyższej listy?')
if co not in produkty:
    print('Nie ma takiego produktu')
    exit(1) # exit powoduje zatrzymanie programu,
    # 0 oznacza, że program zakończył się powodzeniem
    # każdy inny numer oznacza, że coś poszło nie tak
liczba_kg = float(input(f'Ile kilogramów produktu {co} chcesz kupić? '))
kwota = liczba_kg * produkty[co].values()
print(f'Za {liczba_kg} produktu {co} zapłacisz {kwota:.2f} zł')
