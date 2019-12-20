"""### Zadanie 3.3 | Operacje na listach
​
Stwórz następujące funkcje. Każda z nich będzie przyjmowała listę liczb i na tej podstawie wykona odpowiednie operacje i zwróci odpowiedni wynik.
​
```
lista_liczb = [10, 20, 30, 40]
wynik = suma(lista_liczb)

- `roznica_min_max(liczby)` – różnica pomiędzy największą a najmniejszą liczbą w liście; `0` jeśli tablica jest pusta

"""

lista_liczb = [10, 20, 30, 40]
def roznica_min_max(liczby):
    if lista_liczb != []:
        minimum = liczby[0]
        maximum = liczby[0]
        for x in liczby:
            if x < minimum:
                minimum = x
            if x > maximum:
                maximum = x
        return maximum - minimum
    else:
        return 0

print(roznica_min_max(lista_liczb))
print(60*'=')

test = [15,-8,25,20]
def test_roznica_min_max():
    assert roznica_min_max(test) == 33