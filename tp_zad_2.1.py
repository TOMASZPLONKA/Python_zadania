"""
### Zadanie 2.1 | Zagadka matematyczna
​
Program losuje dwie liczby z zakresu od 0 do 99 (patrz poniżej). Podaje te dwie liczby i pyta jaka jest ich suma (nie podaje jej).
Użytkownik ma odgadnąć (no, policzyć w głowie) wynik. Program pyta o wynik wielokrotnie, tak długo, aż użytkownik poda prawidłowy wynik.

"""
import random
A = random.randint(0, 99)
B = random.randint(0, 99)
print(f'Wylosowane liczby to: {A} i {B}')
suma = int(input('Suma liczb A i B to: '))
while True:
    if suma == A + B:
       print(f'Brawo! Suma liczb {A} i {B} równa się {suma}.')
       break
    else:
        print('Niestety to nie jest suma liczb A i B. Spróbuj jeszcze raz.')
        suma = int(input('Suma liczb A i B to: '))