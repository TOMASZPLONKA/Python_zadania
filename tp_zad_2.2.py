"""
### Zadanie 2.2 | Choinka
​
Napisz program, który wczytuje liczbę całkowitą, a następnie na konsolę wypisuje w tylu liniach "choinkę" ze znaków `*`. Np. dla parametru 3 powinno się wypisać:
​
```
    *
  * * *
* * * * *
```
"""

w = 1   # liczba wierszy
g = 1   # liczba gwiazdek w wierszu
l = int(input("Podaj dodatnią liczbę całkowitą: "))     # wprowadzona liczba

while w <= l:
    w = w + 1
    print(f'{("*" * g): ^{l*2-1}}')
    g = g + 2