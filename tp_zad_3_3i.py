"""### Zadanie 3.3 | Operacje na listach
​
Stwórz następujące funkcje. Każda z nich będzie przyjmowała listę liczb i na tej podstawie wykona odpowiednie operacje i zwróci odpowiedni wynik.
​
```
lista_liczb = [10, 20, 30, 40]
wynik = suma(lista_liczb)
```
- `wypisz_podzielne(tab, x)` – wypisuje (`print`) wszystkie te liczby z listy `liczby`, które są podzielne przez `x`
"""

lista_liczb = [10, 20, 30, 40]

def wypisz_podzielne(liczby, x):
    for i in liczby:
        if i % x == 0:
            print(i)

wypisz_podzielne(lista_liczb, 15)
print(60 * '=')

test = [20,25,27,30,36,39]
def test_wypisz_podzielne():
    assert wypisz_podzielne(test,2) == print(20,30,36)
