"""### Zadanie 3.3 | Operacje na listach
​
Stwórz następujące funkcje. Każda z nich będzie przyjmowała listę liczb i na tej podstawie wykona odpowiednie operacje i zwróci odpowiedni wynik.
​
```
lista_liczb = [10, 20, 30, 40]
wynik = suma(lista_liczb)

- `wypisz_wieksze(liczby, x)` – wypisuje (`print()`) wszystkie te liczby z listy `liczby`, które są większe od `x`
"""

lista_liczb = [10, 20, 30, 40]

def wypisz_wieksze(liczby, x):
    for i in liczby:
        if i > x:
            print(i)
wypisz_wieksze(lista_liczb,15)
print(60*'=')

test = [15,-8,25,20]
def test_wypisz_wieksze():
    assert wypisz_wieksze(test,10) == print(15,25,20)