suma_temperatur = 0
numer_dnia = 1
# LICZBA_DNI_TYGODNIA = 7
while numer_dnia <= 7: # LICZBA_DNI_TYGODNIA:
    suma_temperatur += int(input(f'Podaj temperaturę z dnia {numer_dnia}: '))
    numer_dnia +=1

srednia_temperatura = suma_temperatur / 7 # LICZBA_DNI_TYGODNIA

print(f'Średnia temperatura w tym tygodniu to {srednia_temperatura:.2f}')