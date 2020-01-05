"""
# Zadanie 2
Napisz program wyświetlający pogodę dla wskazanej przez użytkownika lokalizacji.
Skorzystaj z modułu `urllib.request`, `json` oraz API MetaWeather.
"""

city = input("Podaj miasto: ")
adres = "https://www.metaweather.com/api/location/search/?query="+city

import json
from urllib.request import urlopen

with urlopen(adres) as plik:
    wynik = json.load(plik)
    id = wynik[0]['woeid']
    #print(id)

with urlopen(f'https://www.metaweather.com/api/location/{id}/') as plik:
    wynik = json.loads(plik.read().decode('utf-8'))

prognozy = wynik['consolidated_weather']
for prognoza in prognozy:
    print(f"Prognoza na dzień {prognoza['applicable_date']}:")
    print(f"\tTemp: min {prognoza['min_temp']:.2f}, max: {prognoza['max_temp']:.2f}")

