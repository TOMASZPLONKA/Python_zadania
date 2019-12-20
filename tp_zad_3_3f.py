"""### Zadanie 3.3 | Operacje na listach
​
Stwórz następujące funkcje. Każda z nich będzie przyjmowała listę liczb i na tej podstawie wykona odpowiednie operacje i zwróci odpowiedni wynik.
​
```
lista_liczb = [10, 20, 30, 40]
wynik = suma(lista_liczb)

- `pierwsza_wieksza(liczby, x)` – zwraca (`return`) pierwszą znalezioną w `liczby` liczbę większą od `x`; zwraca `None`, jeśli takiej liczby tam nie ma
"""

lista_liczb = [10, 20, 30, 40]

def pierwsza_wieksza(liczby, x):
    for i in liczby:
        if i > x:
            return i

print(pierwsza_wieksza(lista_liczb, 50))
print(60 * '=')


test = [5,15,80,40]
def test_pierwsza_wieksza():
    assert pierwsza_wieksza(test,60) == 80