liczby= [-5, -10, 6, -11, 1, 0, 8, -2, -4, -6]

liczby_kopia = list(liczby)
liczby_kopia.sort()

print(liczby)
print(liczby_kopia)

wartosc_minimalna = liczby_kopia[0]
wartosc_maksymalna = liczby_kopia[-1]

klucz_wartosci_minimalnej = liczby.index(wartosc_minimalna)
klucz_wartosci_maksymalnej = liczby.index(wartosc_maksymalna)

print(klucz_wartosci_minimalnej)
print(klucz_wartosci_maksymalnej)

tmp = liczby[klucz_wartosci_minimalnej]
liczby[klucz_wartosci_minimalnej] = liczby[klucz_wartosci_maksymalnej]
liczby[klucz_wartosci_maksymalnej] = tmp

print(liczby)

