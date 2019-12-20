"""### Zadanie 3.3 | Operacje na listach
​
Stwórz następujące funkcje. Każda z nich będzie przyjmowała listę liczb i na tej podstawie wykona odpowiednie operacje i zwróci odpowiedni wynik.
​
```
lista_liczb = [10, 20, 30, 40]
wynik = suma(lista_liczb)

- `max(liczby)` – zwraca największą wartość z listy `liczby`
"""
lista_liczb = [10, 20, 30, 40]

def max(liczby):
    wynik = None
    for x in liczby:
        if wynik == None or x > wynik:
            wynik = x
    return wynik

print(max(lista_liczb))

test = [10,100,-50,250]

def test_max():
    assert max(test) == 250