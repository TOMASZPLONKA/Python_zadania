"""### Zadanie 3.3 | Operacje na listach
​
Stwórz następujące funkcje. Każda z nich będzie przyjmowała listę liczb i na tej podstawie wykona odpowiednie operacje i zwróci odpowiedni wynik.
​
```
lista_liczb = [10, 20, 30, 40]
wynik = suma(lista_liczb)
```
`znajdz_wspolny(liczby1, liczby2)` – zwraca element (liczbę), który występuje zarówno w liście `liczby1`, jak i `liczby2one`, jeśli takiej liczby tam nie ma
"""


liczby1 = [2, 3, 5, 10, 15, 20]
liczby2 = [2, 8, 15, 21, 25]
def znajdz_wspolny(liczby1, liczby2):
    for i in liczby1:
        if i in liczby2:
            print(i)

znajdz_wspolny(liczby1, liczby2)

liczby_a = [1,6,10,8,18,-8]
liczby_b = [5,18,25,10,0]
def test_znajdz_wspolny():
    assert znajdz_wspolny(liczby_a,liczby_b) == print(18,10)


