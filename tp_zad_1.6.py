"""
### Zadanie 1.6 | Bilety (ok. 1 godz.)
​
Założenia:
	- 0-6   - wiek przedszkolny - cena biletu: 0
	- 7-17  - wiek szkolny      - cena biletu: 2.28
	- 18-64 - wiek dorosły      - cena biletu: 3.80
	- +65   - wiek emerytalny   - cena biletu: 1.90
​
Napisz program, który przyjmuje dwie informacje: jaki jest wiek osoby kupującej bilety i ile biletów chce kupić. 
​
Na tej podstawie i powyższych założeń policz ile zapłaci za bilety, które chce kupić.
Wczytywanie danych i ich wyświetlenie zrealizuj za pomocą konsoli.
"""

bilet_D = 0.0
bilet_U = 2.28
bilet_N = 3.80
bilet_S = 1.90
darmowe = list()
ulgowe = list()
normalne = list()
dla_seniorow = list()

licznik = 1
liczba_biletow = int(input("Ile biletów chcesz kupić: "))
while liczba_biletow >= licznik:
    dane = int(input("Podaj wiek posiadacza biletu: "))
    if dane < 7:
        darmowe.append(dane)
    elif 7 <= dane < 18:
        ulgowe.append(dane)
    elif 18 <= dane < 65:
        normalne.append(dane)
    else:
        dla_seniorow.append(dane)
    licznik = licznik + 1
koszt = len(darmowe) * bilet_D + len(ulgowe) * bilet_U + len(normalne) * bilet_N + len(dla_seniorow) * bilet_S

print(f'Koszt zakupionych biletów to: {koszt:.2f} zł')

"""
dlaczego w niektórych przypadkach (jakich? - wydaje mi się, że chodzi o liczby nieparzyste) bez dodania":.2f" 
wynik wyświetla się w postaci np.: 9.879999999999999, mimo że wszystkie części składowe wzoru na koszt są prawidłowe
"""





