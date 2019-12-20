"""### Zadanie 3.3 | Operacje na listach
​
Stwórz następujące funkcje. Każda z nich będzie przyjmowała listę liczb i na tej podstawie wykona odpowiednie operacje i zwróci odpowiedni wynik.
​
```
lista_liczb = [10, 20, 30, 40]
wynik = suma(lista_liczb)
```
- `pierwsza_podzielna(liczby, x)` – zwraca (`return`) pierwszą znalezioną w `liczby` liczbę podzielną przez `x`; zwraca `None`, jeśli takiej liczby tam nie ma
"""

lista_liczb = [10, 20, 30, 40]
def pierwsza_podzielna(liczby, x):
    for i in liczby:
        if i % x == 0:
            return i

print(pierwsza_podzielna(lista_liczb, 20))
print(60 * '=')

test = [5,9,-8,90]
def test_pierwsza_podzielna():
    assert pierwsza_podzielna(test,15) == 90