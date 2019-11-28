"""
### Zadanie 1.4 | Opłata hotelowa (ok 1,5 godz.)
​
Potem napisz taki program: użytkownik podaje swój wiek i ile nocy spędzi w hotelu, a program wylicza, ile trzeba zapłacić.

Zasady są takie:
- nieletni (poniżej 18 roku życia) płacą 100 zł za noc
- dorośli (ci, którzy mają przynajmniej 18 lat ale mniej niż 65 lat) płacą:
	- 200 zł za noc, jeśli nocują jedną noc
	- 180 zł za noc, jeśli nocują przynajmniej dwie ale mniej niż pięć nocy
	- 150 zł za noc, jeśli nocują pięć lub więcej nocy
- emeryci (ci, którzy mają przynajmniej 65 lat), płacą jak dorośli, ale z 10% zniżki
​
Przykładowo: jeśli użytkownik ma 70 lat i spędzi w hotelu dziesięć nocy, zapłaci 150 zł za noc z 10% zniżki, czyli 150-15 zł za noc,
czyli 135 zł za noc, czyli 1350 zł. """

cena_nieletni = 100
cena_dorośli_1 = 200
cena_dorośli_2 = 180
cena_dorośli_3 = 150

liczba_dni = int(input('Podaj liczbę dni: '))
wiek = int(input('Podaj swój wiek: '))

if wiek < 18:
    koszt = liczba_dni * cena_nieletni
    print(f'Za pobyt w hotelu zapłacisz {koszt} zł')
elif 18 <= wiek < 65:
    if 2 <= liczba_dni < 5:
        koszt = liczba_dni * cena_dorośli_2
        print(f'Za pobyt w hotelu zapłacisz {koszt} zł')
    elif liczba_dni >= 5:
        koszt = liczba_dni * cena_dorośli_3
        print(f'Za pobyt w hotelu zapłacisz {koszt} zł')
    else:
        koszt = liczba_dni * cena_dorośli_1
        print(f'Za pobyt w hotelu zapłacisz {koszt} zł')
else:
    if 2 <= liczba_dni < 5:
        koszt = liczba_dni * (cena_dorośli_2 - cena_dorośli_2 * 0.1)
        print(f'Za pobyt w hotelu zapłacisz {koszt} zł')
    elif liczba_dni >= 5:
        koszt = liczba_dni * (cena_dorośli_3 - cena_dorośli_3 * 0.1)
        print(f'Za pobyt w hotelu zapłacisz {koszt} zł')
    else:
        koszt = liczba_dni * (cena_dorośli_1 - cena_dorośli_1 * 0.1)
        print(f'Za pobyt w hotelu zapłacisz {koszt} zł')


