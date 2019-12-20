"""### Zadanie 3.3 | Operacje na listach
​
Stwórz następujące funkcje. Każda z nich będzie przyjmowała listę liczb i na tej podstawie wykona odpowiednie operacje i zwróci odpowiedni wynik.
​
```
lista_liczb = [10, 20, 30, 40]
wynik = suma(lista_liczb)
```
​
- `suma(liczby)` - zwraca sumę liczb z listy `liczby`
- `srednia(liczby)` - zwraca średnią wartość z listy `liczby`
- `max(liczby)` – zwraca największą wartość z listy `liczby`
- `roznica_min_max(liczby)` – różnica pomiędzy największą a najmniejszą liczbą w liście; `0` jeśli tablica jest pusta
- `wypisz_wieksze(liczby, x)` – wypisuje (`print()`) wszystkie te liczby z listy `liczby`, które są większe od `x`
- `pierwsza_wieksza(liczby, x)` – zwraca (`return`) pierwszą znalezioną w `liczby` liczbę większą od `x`; zwraca `None`, jeśli takiej liczby tam nie ma
- `suma_wiekszych(liczby, x)` – zwraca (`return`) sumę liczb z listy `liczby`, które są większe niż `x`
- `ile_wiekszych(liczby, x)` – liczy ile elementów listy `liczby` jest większych od liczby `x`
- `wypisz_podzielne(tab, x)` – wypisuje (`print`) wszystkie te liczby z listy `liczby`, które są podzielne przez `x`
- `pierwsza_podzielna(liczby, x)` – zwraca (`return`) pierwszą znalezioną w `liczby` liczbę podzielną przez `x`; zwraca `None`, jeśli takiej liczby tam nie ma
- `znajdz_wspolny(liczby1, liczby2)` – zwraca element (liczbę), który występuje zarówno w liście `liczby1`, jak i `liczby2`; zwraca `None`, jeśli takiego elementu nie ma
"""

lista_liczb = [10, 20, 30, 40]


def suma(liczby):
    wynik = 0
    for x in liczby:
        wynik = wynik + x
    return wynik

print(suma(lista_liczb))
print(60*'=')

def srednia(liczby):
    for x in liczby:
        return suma(lista_liczb)/len(lista_liczb)


print(srednia(lista_liczb))
print(60*'=')

def max(liczby):
    wynik = None
    for x in liczby:
        if wynik == None or x > wynik:
            wynik = x
    return wynik

print(max(lista_liczb))
print(60*'=')

def roznica_min_max(liczby):
    if lista_liczb != []:
        minimum = liczby[0]
        maximum = liczby[0]
        for x in liczby:
            if x < minimum:
                minimum = x
            if x > maximum:
                maximum = x
        return maximum - minimum
    else:
        return 0

print(roznica_min_max(lista_liczb))
print(60*'=')

def wypisz_wieksze(liczby, x):
    for i in liczby:
        if i > x:
            print(i)
wypisz_wieksze(lista_liczb,15)
print(60*'=')

def pierwsza_wieksza(liczby, x):
    for i in liczby:
        if i > x:
            return i



print(pierwsza_wieksza(lista_liczb, 50))
print(60 * '=')

def suma_wiekszych(liczby, x):
    wynik = 0
    for i in liczby:
        if i > x:
            wynik = wynik + i
    return wynik

print(suma_wiekszych(lista_liczb, 15))
print(60 * '=')

def ile_wiekszych(liczby, x):
    wynik = 0
    for i in liczby:
        if i > x:
            wynik = wynik + 1
    return wynik

print(ile_wiekszych(lista_liczb, 15))
print(60 * '=')

def wypisz_podzielne(liczby, x):
    for i in liczby:
        if i % x == 0:
            print(i)

wypisz_podzielne(lista_liczb, 15)
print(60 * '=')


def pierwsza_podzielna(liczby, x):
    for i in liczby:
        if i % x == 0:
            return i

print(pierwsza_podzielna(lista_liczb, 20))
print(60 * '=')

liczby1 = [2, 3, 5, 10, 15, 20]
liczby2 = [2, 8, 15, 21, 25]
def znajdz_wspolny(liczby1, liczby2):
    for i in liczby1:
        if i in liczby2:
            print(i)

znajdz_wspolny(liczby1, liczby2)