"""
### Zadanie 2.3
​
Napisz program, który odczytuje od użytkownika wiele liczb.
​
Program powinien wyliczyć i na końcu wypisać następujące statystyki:
​
- liczba podanych liczb (ile sztuk),
- suma,
- średnia,
- minimum
- maksimum

"""

minimum = None
maximum = None
suma = None
srednia = None
liczby = list()

while True:
    dane_wejsciowe = input('Podaj liczbę: ')
    if (dane_wejsciowe.lstrip('-').replace('.','0',1).isdecimal() and dane_wejsciowe != '.' and dane_wejsciowe != '-.'):
        # to taki mój sposób na to żeby można było wprowadzić liczby dziesiętne
        liczba = float(dane_wejsciowe)
        liczby.append(liczba)
        if minimum == None or liczba < minimum:
            minimum = liczba
        if maximum == None or liczba > maximum:
            maximum = liczba
    else:
        if dane_wejsciowe == 'koniec':
            break
        else:
            print('To nie jest liczba.')
            continue
if liczby != []:
    suma = sum(liczby)
    srednia = suma / len(liczby)

print(f'Liczba wprowadzonych danych: {len(liczby)}')
if suma != None:
    print(f'Suma = {suma}')
    print(f'Średnia = {round(srednia,2)}')
    print(f'Znaleziono minimum = {minimum} i maximum = {maximum}')
else:
    print('Brak możliwości obliczenia sumy i średniej oraz wyznaczenia minimum i maximum.')
