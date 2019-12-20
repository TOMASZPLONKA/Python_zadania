"""### Zadanie 3.3 | Operacje na listach
​
Stwórz następujące funkcje. Każda z nich będzie przyjmowała listę liczb i na tej podstawie wykona odpowiednie operacje i zwróci odpowiedni wynik.
​
```
lista_liczb = [10, 20, 30, 40]
wynik = suma(lista_liczb)
```
- `srednia(liczby)` - zwraca średnią wartość z listy `liczby`

"""

lista_liczb = [10, 20, 30, 40]


def suma(liczby):
    wynik = 0
    for x in liczby:
        wynik = wynik + x
    return wynik


def srednia(liczby):
    for x in liczby:
        return suma(lista_liczb)/len(lista_liczb)


print(srednia(lista_liczb))
print(60*'=')

lista_liczb = [15,80,45,-20]

def test_srednia():
    assert srednia(lista_liczb) == 30