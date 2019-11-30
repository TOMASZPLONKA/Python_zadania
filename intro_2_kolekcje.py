# KOLEKCJE

#=== TUPLA === w nawiasach okrągłych

a = (1, 2, 3)
b = (1, 3.14, 'ala', True)
c = ( (1,2), ('a','b','c') )
print(a)
print(b)
print(c)

d = (100) # UWAGA! Python potraktował to jako int a nie tuplę
e = (100,)
print(type(e))
f = ()
print(type(f))
g = tuple()
print(type(g))

# wyciąganie wartości z tupli

x = ('a','b','c','d','e','f','g','h','i','j')
print(x[0]) # a
print(x[5]) # f
print(x[1:3]) # b, c - przedział lewostronnie zamknięty i prawostronnie otwarty
print(x[2:6]) # c, d, e, f
print(x[-1]) # j
print(x[-4:-1]) # g, h, i
print(x[1:]) # wszsytkie elementy od drugiego
print(x[:4]) # wszystkie elementy do czwartego (prawostronnie otwarte)
print(x[::2]) # wyciąganie co drugiego elementu
print(x[::-2]) # wyciąganie co drugiego elementu od tyłu

# przydatne petody
print(len(x)) # - zlicza elementy tupli
print('b' in x) # - czy b jest w tupli x
print('b' in x)
f = (1, 2, 3, 4, 5)
print(min(f))
print(max(f))
print(sum(f))

c = a + b # suma 2 tupli
print(c)

d= a * 3
print(d)

a = ('a', 'b', 'c')
print(a[2])

#=== LISTA === w nawiasach kwadratowych

a= [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print(a[0])
print(a[-1])
a[0]=-1
print(a[0])
a.append(110) # dodanie elementu na koniec listy
print(a)
a.insert(1,12) # dodanie elementu na drugi indeks - cała reszta przesunięta
print(a)

a[0:2] = [1,2] # podmiana na pierwsze 2 elementy nowych
print(a)
a[0:2] = [1,2,3,4]
print(a)

a.extend([120, 130, 140]) # dodanie kilku elementów na koniec listy, append potraktuje to jako 1 element (zagnieżdżenie)
print(a)

del(a[0])
print(a)

del(a[0:2])
print(a)

del(a[-2:])
print(a)

del(a[:]) # usunięcie wsazystkich elementów
print(a)

lista = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
i = 0
while i < len(lista):
    print(lista[i])
    i= i+1

# PĘTLA FOR

for x in lista:
    print(x)

for x in range(10): # 10 liczb
    print(x)

for x in range(4,10): # od 4 do 10 liczby
    print(x)

for x in range(4,10,2): # od 4 do 10 liczby co 2
    print(x)


#=== NAPISY ===
napis = 'Ala ma kota a kot ma kompilator'
print(napis[0])
print(napis[0:3])
print(napis[4:])
print(napis[::-1])
print(napis.lower())
print(napis.upper())
print(napis.title()) # każda litera słowa z wielkiej litery
print(napis.capitalize()) # każda pierwsza litera w napisie z wielkiej litery

print(napis.split()) # standardowo jest po spacji, ale można sobie samodzielnie zdefiniować
print(napis.split('a'))

po_podziale = napis.split()
po_scaleniu = '<->'.join(po_podziale)
print(po_scaleniu)

print(napis.count('a'))
print(napis.index('a')) # pierwszy indeks w napisie, gdzie występuje dany znak
print(napis.find('a')) # pierwszy indeks w napisie, gdzie występuje dany znak
print(napis.find('z'))

# Szukanie palindromu
napis ="Kamil Ślimak"
napis = napis.lower()
napis = napis.replace(' ','')

print(napis)
print(napis[::-1])
print(napis == napis[::-1])
print(())

### SŁOWNIK

slownik = {
    'ala': 10,
'ela': 20,
'ula': 30,
1: 'kot', # hash z 1 = 1
2.5: 1000,
True: 5000, # hash z True = 1
(1,2): 6000,
}

print(slownik)
print(slownik['ela'])
print(slownik[1])
print(slownik[2.5])
print(slownik[True])
print( 'ala'.__hash__() )
print( (1,2).__hash__() )

slownik['ela'] = 1234
print(slownik)

# możemy sprawdzić czy klucz znajduje się w danym słowniku

print('ala' in slownik)
print('krysia' in slownik)

# inny sposób na pobieranie elementów
print(slownik.get('ala'))
print(slownik.get('krysia'))
print(slownik.get('krysia', 123))

# jak usunąć elementy ze słownika

print(slownik['ala'])
del(slownik['ala'])
print(slownik)

# pobieranie i usuwanie elementu ze słownika, za jednym razem

wartosc = slownik.pop('ela')
print(wartosc)
print(slownik)
print()

# popitem - wyciąga i usuwa ostatnią wartość - od Pythona 3.7., wcześniej był to losowy element
wartosc = slownik.popitem()
print(wartosc)
print(slownik)
print()


# iterowanie po słowniku przy użyciu for

for x in slownik: # pod x = klucz ze słownika
    print(x)

print()

for x in slownik:
    print(x, "|", slownik[x])

print()

for x in slownik.keys():
    print(x)

print()

for x in slownik.values():
    print(x)

print()

print(slownik.keys()) # zwraca klucze - lista
print(slownik.values()) # zwraca wartości - lista
print(slownik.items()) # klucz i wartość, pogrupowane w pary - lista tupli

print()

a,b = (10,20)
print(a)
print(b)

print()

# zmienne w pętli - klucz i wartość, mogą się nazywać dowolnie
for klucz, wartosc in slownik.items():
    print(klucz, '->',wartosc)

print()

## ZBIÓR

zbior = {10, 20, 30, 40, 50}
print(zbior)

zbior.add(60) #dodanie elementu
print(zbior)

zbior.remove(60) # usunięcie elementu
print(zbior) # jezeli chcemy usunąć element, którego nie ma, to wyrzuci błąd

zbior.discard(60) # jezeli chcemy usunąć element, którego nie ma, to nic się nie stanie
print(zbior)

# print(zbior[0]) zbiór nie obsługuje dostępu do pojedynczego elementu
for element in zbior:
    print(element)
print(len(zbior))
print()
a = {1, 2, 3}
b = {1, 2, 4, 5}

print(a | b) # suma zbiorów
print(a.union(b)) # suma zbiorów - inna metoda
print(a & b) # iloczyn (część wspólna)
print(a.intersection(b)) # iloczyn - inna metoda
print(a - b) # różnica zbiorów
print(b.difference(a)) # różnica zbiorów - inna metoda
print(a ^ b) # różnica symetryczna - od sumy zbiorów a i b odejmujemy część wspólną zbiorów a i b
print(b.symmetric_difference(a)) # różnica symetryczna - od sumy zbiorów a i b odejmujemy część wspólną zbiorów a i b

# czy zbiory a i b są rozłączne, czyli nie mają wspólnych elementów
print(a.isdisjoint(b))
# czy a jest podzbiorem b
print(a <= b) # zbiór a może być taki sam jak zbiór b, bo mamy mniejsze lub równe
print(a < b) # zbiory nie mogą być równe

c = {3,4}
d = {3,4}
print(c <= d) # True
print(c < d) # False
print()
# czy a jest nadzbiorem b
print(a >= b)
print(a > b)
print(c >= d)
print(c > d)
print()

# dotychczasowe operacje powodowały utworzenie nowego zbioru będącego wynikiem danej operacji, ale zbiory można modyfikować
a = {1, 2, 3}
b = {1, 2, 4, 5}

#a |= b
a.update(b)
print(a)

a = {1, 2, 3}
b = {1, 2, 4, 5}

a &=b
#a.intesection_update(b)
print(a)

a = {1, 2, 3}
b = {1, 2, 4, 5}
#a -=b
a.difference_update(b)
print(a)

a = {1, 2, 3}
b = {1, 2, 4, 5}
a.symmetric_difference_update(b)
# a ^=b
print(a)
print()

### WYRAŻENIA LISTOWE
# mogą być i wyrażenia zbiorowe, wyrażenia słownikowe
# list comprehension, dict comprehension, set comprehension

dane = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
wynik = []

for wartosc in dane:
    wynik.append( wartosc ** 2)
print(wynik)

# zrobienie tego samego za pomocą list comprehension
wynik = [ wartosc ** 2 for wartosc in dane]
print(wynik)

liczby = { x for x in range (0,101,2)} # set comprehension
print(liczby)
print()

pensje = [1000, 2000, 2500, 1500, 5000]
# na podstawie pensji policzyć kwotę do wypłaty dla pracownika, czyli trzeba potrącić podatek
do_wyplaty = []
for pensja in pensje:
    do_wyplaty.append((round(pensja * 0.81,2)))
print(do_wyplaty)

do_wyplaty = [round(pensja * 0.81,2) for pensja in pensje]
print(do_wyplaty)

# premie -> jeżeli pensja jest mniejsza lub równa 2000 to dajemy 10% premii, jak większa to nie ma premii
premie = []
for pensja in pensje:
    if pensja <= 2000:
        premie.append(0.10)
    else:
        premie.append(0)
print(premie)

premie = [ 0.10 if pensja <= 2000 else 0 for pensja in pensje]
print(premie)
# wartość premii, metoda zip (spinanie dwóch list)
print(list( zip(do_wyplaty, premie)))
wartosc_premii = [ pensja * premia for pensja, premia in zip(do_wyplaty, premie)]
print(wartosc_premii)
# policzyć kwotę do wypłaty, czyli kwota netto + wartość premii
do_wyplaty_z_premia = [kwota_do_wyplaty + kwota_premii for kwota_do_wyplaty, kwota_premii in zip(do_wyplaty, wartosc_premii)]
print(do_wyplaty_z_premia)

# potrzebuję listę pracowników, którym trzeba wypłacić więcej niż 2000
pracownicy_drozsi = []
for pensja in do_wyplaty_z_premia:
    if pensja > 2000:
        pracownicy_drozsi.append(pensja)
print(pracownicy_drozsi)
pracownicy_drozsi = [ pensja for pensja in do_wyplaty_z_premia if pensja > 2000]
print(pracownicy_drozsi)



