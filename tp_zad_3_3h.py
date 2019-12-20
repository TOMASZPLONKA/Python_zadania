"""### Zadanie 3.3 | Operacje na listach
​
Stwórz następujące funkcje. Każda z nich będzie przyjmowała listę liczb i na tej podstawie wykona odpowiednie operacje i zwróci odpowiedni wynik.
​
```
lista_liczb = [10, 20, 30, 40]
wynik = suma(lista_liczb)
```

- `ile_wiekszych(liczby, x)` – liczy ile elementów listy `liczby` jest większych od liczby `x`
"""

lista_liczb = [10, 20, 30, 40]

def ile_wiekszych(liczby, x):
    wynik = 0
    for i in liczby:
        if i > x:
            wynik = wynik + 1
    return wynik

print(ile_wiekszych(lista_liczb, 15))
print(60 * '=')

test = [-8,8,10,40,3]
def test_ile_wiekszych():
    assert ile_wiekszych(test,2) == 4