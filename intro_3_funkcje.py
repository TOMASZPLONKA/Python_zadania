### FUNKCJE

def powiedz_czesc():
    print("Cześć!")

powiedz_czesc()
powiedz_czesc()

def powiedz_czesc_komus(imie, nazwisko):
    print(f'Cześć {imie} {nazwisko}!')

powiedz_czesc_komus("Piotr", "Nowak")
powiedz_czesc_komus("Tomasz","Kowalski")

# powyższe funkcje nic nie zwracają, mają "efekt uboczny", że coś zostanie wypisane na konsolę

# funkcje mogą zwracać wartości, tzn. możemy zwrócić wartość, która będzie wynikiem działania funkcji

def suma(a, b):
    return a + b # komenda return powoduje zwrócenie jakiejś wartości z funkcji

wynik = suma(2,3)
print(wynik)

def iloczyn(a, b):
    """
    To jest docstring. Mówi co dana funkcja robi. Jest to element dokumentacji.
    :param a:
    :param b:
    :return:
    """
    return  a * b
wynik = iloczyn(2, 3)
print(wynik)

def iloczyn(x: int, y: int): # type hinting - sugerowanie jaki typ argumentów wprowadzić do funkcji
    """
    To jest type hinting.
    :param x:
    :param y:
    :return:
    """
    return x * y
wynik = iloczyn(3,4.5) # podświetla jak typ danych jest inny niż sugerowany
print(wynik)

napis = 'ala ma kota'
print(napis.count('a'))

# ARGUMENTY DOMYŚLNE W FUNKCJI

def opakowywacz(napis, start = '>', end= '<'):
    return start + napis + end
# uruchamianie funkcji z przekazaniem argumentów w sposób pozycyjny, muszą być podane wszystkie obligatoryjne argumenty,
# nie trzeba wpisywać domyślnych, musi być zachowana kolejność
print(opakowywacz('ala ma kota','>>>','<<<'))
print(opakowywacz('kot ma kompilator')) # start i end mają wartości domyślne
print(opakowywacz('ala ma kota','>>>')) # zmiana tylko jednej wartości domyślnej

# uruchamianie funkcji odbywa się poprzez przekazanie argumentów nazwanych, tutaj nie musi być zachowana kolejność
print(opakowywacz(start='>>', end ='<<', napis = 'ala ma kota'))
print(opakowywacz(napis = 'ala ma kota'))

# uruchamianie funkcji z przekazaniem argumentów w sposób pozycyjny i nazwany
print(opakowywacz('ala ma kota', end= '---',start= '---')) # jak mieszamy 2 sposoby, to najpierw podajemy argumenty pozycyjne, a potem nazwane