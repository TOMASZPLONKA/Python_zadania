"""### Zadanie 1.5 | Pole trójkąta (ok. 1 godz.)
​
Program, który odczytuje trzy liczby, sprawdza czy liczby te mogą stanowić boki trójkąta
(np. z 2, 2 i 5 nie da się ułożyć trójkąta, prawa?), a jeśli mogą, oblicza pole powierzchni trójkąta o takich bokach.

P=p(p−a)(p−b)(p−c)−−−−−−−−−−−−−−−−−√

"""
dane = list()
while True:
    while len(dane) <= 2:
        bok = float(input('Podaj bok trójkąta: '))
        dane.append(bok)

    import math
    p = (dane[0] + dane[1] + dane[2]) / 2
    wer = (p * (p-dane[0]) * (p-dane[1]) * (p-dane[2]))

    if wer > 0: # sprawdzenie czy liczba podpierwiastkowa jest większa od 0 - nie ma pierwiastka z liczby ujemnej
        pole = math.sqrt(p * (p-dane[0]) * (p-dane[1]) * (p-dane[2]))
        print(f'Pole trójkąta = {pole}')
        break
    else:
        print(f'Podane liczby nie stanowią boków trójkąta')
        dane = list()
        continue







