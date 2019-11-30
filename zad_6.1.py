liczby= [-5, -10, 6, -11, 1, 0, 8, -2, -4, -6]
indeks_min = None
indeks_max = None

for indeks, wartosc in enumerate(liczby):
    if indeks_min is None or wartosc < liczby[indeks_min]:
        indeks_min = indeks
    if indeks_max is None or wartosc > liczby[indeks_max]:
        indeks_max = indeks

print(indeks_min)
print(indeks_max)

liczby[indeks_min],liczby[indeks_max] = liczby[indeks_max], liczby[indeks_min]
print(liczby)

liczby = [-5, -10, 6, -11, 1, 0, 8, -2, -4, -6]

liczba_minimalna = liczby[0]
liczba_maksymalna = liczby[0]

for element in liczby:
    if element < liczba_minimalna:
        liczba_minimalna = element
    if element > liczba_maksymalna:
        liczba_maksymalna = element

print(liczba_minimalna)
print(liczba_maksymalna)

