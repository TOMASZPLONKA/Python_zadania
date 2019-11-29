"""
### Zadanie 2.1 | Zagadka matematyczna
​
Program losuje dwie liczby z zakresu od 0 do 99 (patrz poniżej). Podaje te dwie liczby i pyta jaka jest ich suma (nie podaje jej).
Użytkownik ma odgadnąć (no, policzyć w głowie) wynik. Program pyta o wynik wielokrotnie, tak długo, aż użytkownik poda prawidłowy wynik.

"""
import random
a = random.randint(0, 99)
b = random.randint(0, 99)
print(f'Wylosowane liczby to: {a} i {b}')
suma = int(input('Suma liczb A i B to: '))
while True:
    if suma == a + b:
       print(f'Brawo! Suma liczb {a} i {b} równa się {suma}.')
       break
    else:
        print('Niestety to nie jest suma liczb A i B. Spróbuj jeszcze raz.')
        suma = int(input('Suma liczb A i B to: '))
