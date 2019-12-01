from random import randint # import funkcji randint z pakietu random

gracz_x = 1
gracz_y = 1

skarb_x = 5
skarb_y = 5

liczba_krokow = 0
minimalna_liczba_krokow = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)

while True:
    print(f'Twoja pozycja x = {gracz_x:2}, y = {gracz_y:2}')

    odleglosc_przed_ruchem = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)

    kierunek = input("Podaj kierunek (W,S,A,D): ")
    if kierunek == 'W':
        gracz_y = gracz_y + 1
    elif kierunek == 'S':
        gracz_y = gracz_y -1
    elif kierunek == 'A':
        gracz_x = gracz_x - 1
    elif kierunek == 'D':
        gracz_x = gracz_x + 1
    else:
        print('Niepoprawny kierunek')
        continue
    odleglosc_po_ruchu = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)

    liczba_krokow +=1
    if liczba_krokow > (minimalna_liczba_krokow * 2):
        skarb_x = randint (0,10)
        skarb_y = randint (0,10)
        minimalna_liczba_krokow = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)
        liczba_krokow = 0

    if gracz_x < 0 or gracz_x > 10 or gracz_y < 0 or gracz_y > 10:
        print(f'Jesteś poza planszą. Koniec gry Wykonana liczba kroków = {liczba_krokow}')
        break

    if gracz_x == skarb_x and gracz_y == skarb_y:
        print('Brawo! Znalazłeś skarb!')
        break
    if randint (1,5)  != 5:
        if odleglosc_po_ruchu < odleglosc_przed_ruchem:
            print('Ciepło')
        else:
            print('Zimno')

