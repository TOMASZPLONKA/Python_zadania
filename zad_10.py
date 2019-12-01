liczba_1 = int(input("Podaj liczbę 1: "))
liczba_2 = int(input("Podaj liczbę 2: "))
operacja = (input("Podaj operację (=, -, *, /): "))

if operacja == '+':
    wynik = liczba_1 + liczba_2
elif operacja == '-':
    wynik = liczba_1 - liczba_2
elif operacja == '*':
    wynik = liczba_1 * liczba_2
elif operacja == '/':
    wynik = liczba_1 / liczba_2
else:
    wynik = None


if wynik == None:
    print('Podałeś nieprawidłowe dane')
else:
    print(f'Wynik: {wynik}')
