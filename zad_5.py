#funkcja input - zwraca zawsze typ string

miasto_a = input("Miasto A: ")
miasto_b = input("Miasto B: ")
dystans = int(input(f'Dystans {miasto_a} - {miasto_b}: '))
# print(dystans)
# print(type(dystans))
cena = float(input('Cena paliwa: '))
spalanie = float (input('Spalanie na 100 km: '))
koszt_przejazdu = (dystans * spalanie / 100 * cena)

# format -specifier
print (f'Koszt przejazdu {miasto_a} - {miasto_b} to {koszt_przejazdu} PLN')
print (f'Koszt przejazdu {miasto_a} - {miasto_b} to {koszt_przejazdu:.2f} PLN')
print (f'Koszt przejazdu {miasto_a} - {miasto_b} to {koszt_przejazdu:10.2f} PLN') # podaje 10 znaków

# zaokrąglenie
# koszt_przejazdu = round(dystans * spalanie / 100 * cena, 2)