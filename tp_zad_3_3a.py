"""### Zadanie 3.3 | Operacje na listach
​
Stwórz następujące funkcje. Każda z nich będzie przyjmowała listę liczb i na tej podstawie wykona odpowiednie operacje i zwróci odpowiedni wynik.
​
```
lista_liczb = [10, 20, 30, 40]
wynik = suma(lista_liczb)
```
​
- `suma(liczby)` - zwraca sumę liczb z listy `liczby`"""

lista_liczb = [10, 20, 30, 40]


def suma(liczby):
    wynik = 0
    for x in liczby:
        wynik = wynik + x
    return wynik

print(suma(lista_liczb))
print(60*'=')

test = [100, -20, 50, -40]
def test_suma():
    assert suma(test) == 90
