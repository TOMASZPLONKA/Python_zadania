liczba = int(input("Podaj liczbę: "))

wynik = (liczba % 2 != 0 and liczba % 3 == 0 and liczba > 10) or liczba == 7

# proces wyliczania złożonego wyrażenia (takiego, które nie jest zwykłą wartością) nazywamy ewaluacją
print(f'Wynik: {wynik}')