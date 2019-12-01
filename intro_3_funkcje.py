### FUNKCJE

def powiedz_czesc():
    print("Cześć!")


powiedz_czesc()
powiedz_czesc()


def powiedz_czesc_komus(imie, nazwisko):
    print(f'Cześć {imie} {nazwisko}!')


powiedz_czesc_komus("Piotr", "Nowak")
powiedz_czesc_komus("Tomasz", "Kowalski")


# powyższe funkcje nic nie zwracają, mają "efekt uboczny", że coś zostanie wypisane na konsolę

# funkcje mogą zwracać wartości, tzn. możemy zwrócić wartość, która będzie wynikiem działania funkcji

def suma(a, b):
    return a + b  # komenda return powoduje zwrócenie jakiejś wartości z funkcji


wynik = suma(2, 3)
print(wynik)


def iloczyn(a, b):
    """
    To jest docstring. Mówi co dana funkcja robi. Jest to element dokumentacji.
    :param a:
    :param b:
    :return:
    """
    return a * b


wynik = iloczyn(2, 3)
print(wynik)


def iloczyn(x: int, y: int):  # type hinting - sugerowanie jaki typ argumentów wprowadzić do funkcji
    """
    To jest type hinting.
    :param x:
    :param y:
    :return:
    """
    return x * y


wynik = iloczyn(3, 4.5)  # podświetla jak typ danych jest inny niż sugerowany
print(wynik)

napis = 'ala ma kota'
print(napis.count('a'))


# ARGUMENTY DOMYŚLNE W FUNKCJI

def opakowywacz(napis, start='>', end='<'):
    return start + napis + end


# uruchamianie funkcji z przekazaniem argumentów w sposób pozycyjny, muszą być podane wszystkie obligatoryjne argumenty,
# nie trzeba wpisywać domyślnych, musi być zachowana kolejność
print(opakowywacz('ala ma kota', '>>>', '<<<'))
print(opakowywacz('kot ma kompilator'))  # start i end mają wartości domyślne
print(opakowywacz('ala ma kota', '>>>'))  # zmiana tylko jednej wartości domyślnej

# uruchamianie funkcji odbywa się poprzez przekazanie argumentów nazwanych, tutaj nie musi być zachowana kolejność
print(opakowywacz(start='>>', end='<<', napis='ala ma kota'))
print(opakowywacz(napis='ala ma kota'))

# uruchamianie funkcji z przekazaniem argumentów w sposób pozycyjny i nazwany
print(opakowywacz('ala ma kota', end='---',
                  start='---'))  # jak mieszamy 2 sposoby, to najpierw podajemy argumenty pozycyjne, a potem nazwane

### PRINT, jak przekazywać wiele argumentów

print(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


def zliczacz(*args, **kwargs):
    print("args=", args)
    print("kwargs=", kwargs)
    print()


# pusta funkcja
zliczacz()

# tylko argumenty pozycyjne
zliczacz(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)  # zwraca tuplę
# tylko argumenty nazwane
zliczacz(a=1, b=3, c='a', d='ala',
         e=True)  # zwraca słownik, kluczem nazwa argumentu nazwanego, a wartością, wartość tego argumentu
# argumenty pozycyjne i nazwane
zliczacz(1, 2, 3, a=1, b=2, c=True)  # zwraca tuplę i słownik


def fun(a, b, c=10, *args, **kwargs):
    print(a, b, c, args, kwargs)


fun(1, 2)
fun(1, 2, 3, 4, 5, 6, 7)
fun(1, 2, 3, 4, 5, 6, 7, x=1, y=1)

## UWAGA
"""
Funkcja to kolejny typ danych 
"""


def czesc(imie):
    print(f"Cześć {imie}")


czesc("Tomasz")

funkcja_co_mowi_czesc = czesc
funkcja_co_mowi_czesc('Zosia')

moj_print = print
moj_print('Ala ma kota')


def kwadrat(x):
    return x ** 2


print(kwadrat(3))

kwadrat = lambda x: x ** 2
print(kwadrat(4))

square = kwadrat
print(square(5))


def sumator(a, b, c):
    return a + b + c


sumator = lambda a, b, c: a + b + c
print(sumator(10, 20, 30))


# zwracanie  rzeczy z funkcji lambda
def x_mniejsze_od_y(x, y):
    if x < y:
        return True
    else:
        return False


print(x_mniejsze_od_y(2, 3))
print(x_mniejsze_od_y(20, 10))

x_mniejsze_od_y = lambda x, y: x < y
print(x_mniejsze_od_y(2, 3))
print(x_mniejsze_od_y(20, 10))

# lambda bez żadnych parametrów
witaj_swiecie = lambda: "Hello World!"
print(witaj_swiecie())


def wykonaj_operacje_na_liscie(lista, operacja):
    rezultat = []
    for element in lista:
        rezultat.append(operacja(element))

    return rezultat


moja_operacja = lambda x: x ** 2
wynik = wykonaj_operacje_na_liscie([10, 20, 30], moja_operacja)
print(wynik)

# funkcja map
lista = [10, 20, 30, 40]
print(list(map(lambda x: x * 2, lista)))

# filter
lista = [-1, 2, -15, -81, 40, 100]
print(list(filter(lambda x: x > 0, lista)))

# sortowanie
lista = [9, 8, 5, 2, 6, 1]
print(lista)
lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)

lista = [(2, 2), (3, 4), (4, 1), (1, 3)]
print(lista)
lista.sort()
lista.sort(key=lambda x: x[1])  # sortowanie wg drugiego elementu tupli
print(lista)
print()

lista = [(2, 2), (3, 4), (4, 1), (1, 3)]

"""
def komparator(a, b):
     komparator ma zwrócić dla 2 porównywalnych elementów następujące wartości, których użyje metoda sort do sortowania:
    -1 - kiedy a jest mniejsze od b (a powinno być przed b)
     0 - kiedy a i b są równe
     1 - kiedy a jest większe od b (b powinno być przed a)
     

    if a[1] < b[1]:
        return -1
    elif a[1] == b[1]:
        return 0
    else:
        return 1

from functools import cmp_to_key

print(lista)
lista.sort(key=cmp_to_key(kompilator))
print(lista)"""


# co z FALSE

zmienna = 'ala ma kota'
zmienna = '' # F
zmienna = '0' # P
zmienna = 'False' # P
zmienna = 0 # F
zmienna = -1 # P
zmienna = 1 # P
zmienna = () # F
zmienna = (1) # P
zmienna = (False) # F -> bo to nie jest tupla, typ bool
zmienna = (False,False) # P -> to jest tupla
zmienna = []# F
zmienna = {} # F
zmienna = set() # F
zmienna = None # F


if zmienna:
    print("PRAWDA")
else:
    print("FAŁSZ")

