"""### Zadanie 3.3 | Operacje na listach
​
Stwórz następujące funkcje. Każda z nich będzie przyjmowała listę liczb i na tej podstawie wykona odpowiednie operacje i zwróci odpowiedni wynik.
​
```
lista_liczb = [10, 20, 30, 40]
wynik = suma(lista_liczb)
```
​- `suma_wiekszych(liczby, x)` – zwraca (`return`) sumę liczb z listy `liczby`, które są większe niż `x`
"""
lista_liczb = [10, 20, 30, 40]
def suma_wiekszych(liczby, x):
    wynik = 0
    for i in liczby:
        if i > x:
            wynik = wynik + i
    return wynik

print(suma_wiekszych(lista_liczb, 15))
print(60 * '=')

test = [50,70,90,150]

def test_suma_wiekszych():
    assert suma_wiekszych(test,80) == 240