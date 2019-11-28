"""Zadanie 1.1 | Interakcja i proste obliczenia (ok. 2 godz.)
​
A) Napisz program, który prosi użytkownika (przez `input()`), żeby podał, ile kosztuje kilo ziemniaków.
Niech program policzy i wyświetli, ile trzeba będzie zapłacić za pięć kilo ziemniaków.
​
B) Potem napisz program, który prosi użytkownika (przez `input()`), żeby podał, ile kosztuje kilo ziemniaków i ile kilo chce kupić.
Niech program policzy i wyświetli, ile trzeba będzie zapłacić za te ziemniaki.
​
C) Potem napisz program, który prosi użytkownika (przez `input()`), żeby podał, ile kosztuje kilo ziemniaków, ile kilo
ziemniaków chce kupić, ile kosztuje kilo bananów i ile kilo bananów chce kupić. Niech program policzy i wyświetli,
ile trzeba będzie zapłacić za te ziemniaki i banany razem. I niech program sprawdzi i powie, za co trzeba będzie zapłacić więcej -
za banany czy za ziemniaki.
​
"""
## A
cena_ziemniakow = float(input('Podaj cenę kg ziemniaków: '))
cena_5_kg = cena_ziemniakow * 5
print(f'Za 5 kg ziemniaków zapłacisz {cena_5_kg} zł')

## B
cena_ziemniakow = float(input('Podaj cenę kg ziemniaków: '))
ilosc = float(input('Podaj ile chcesz kupić ziemniaków w kg: '))
koszt = cena_ziemniakow * ilosc
print(f'Za {ilosc} kg ziemniaków zapłacisz {koszt} zł')

## C
cena_ziemniakow = float(input('Podaj cenę ziemniaków za kg: '))
cena_bananow = float(input('Podaj cenę bananów za kg: '))
ilosc_z = float(input('Podaj ile chcesz kupić ziemniaków w kg: '))
ilosc_b = float(input('Podaj ile chcesz kupić bananów w kg: '))
koszt = cena_ziemniakow * ilosc_z + cena_bananow * ilosc_b

print(f'Za zakupy zapłacisz {koszt} zł')
if cena_ziemniakow * ilosc_z > cena_bananow * ilosc_b:
    print('Za ziemniaki zapłacisz więcej niż za banany')
elif cena_ziemniakow * ilosc_z < cena_bananow * ilosc_b:
    print('Za banany zapłacisz więcej niż za ziemniaki')
else:
    print('Ziemniaki kosztują tyle samo co banany')




