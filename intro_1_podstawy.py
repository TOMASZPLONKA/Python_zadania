print('Hello World!')

# komentarz do końca linijki

# TYPY DANYCH

# string NAPISY, ciągi znaków, tzw. stringi
# definiujemy w ' lub "
print('Ala ma kota')
print("Ala ma kota")

# int (od integer) LICZBY CAŁKOWITE
# int są nieograniczone, tzn. dowolnie duże (małe) liczby można przechowywać
print(10)
print(-8)

# float - LICZBY ZMIENNOPRZECINKOWE
# float w pythonie jest zaimplementowany poprzez typ double w C

#import sys
#print(sys.float_info) # sprawdzenie ile można przechowywać w typie float

print(3.5) # musi być kropka, a nie przecinek
print(.1) # lub print(0.1)
print(1.) # lub print(1.0)
# print(1.) lub print(1) to są różne typy danych (float i int)
print(type(1))
print(type(1.0))

# bool, boolean, typ boolowski
# przyjmuje wartości TRUE lub FALSE, pisać z wielkiej litery

print(True)
print(False)
print(type(True))

# NONE, null, wartość oznaczająca brak wartości, pisać z wielkiej litery
print(None)

# True, False, None zawsze z wielkiej litery

# OPERATORY
print(10+3)
print(10-3)
print(10*3)
print(10/3) # wynik 3.3333333333333335
print(10//3) # dzielenie całkowito liczbowe, wynik 3 - ucina część ułamkową
print(10%3) # reszta z dzielenia
print(10**3) # - potęgowanie
print('Ala'+ ' ma kota') # konkatenacja
print('Ala' * 10) # mnożenie znaków (powtórzenie dziesięciokrotne ciągu znaków

print('ala ma \'kota\' a kot ma kompilator') # użycie znaku ' w ciągu znaków
print('ala ma "kota" a kot ma kompilator') # inny sposób -użycie cudzysłowu
print("ala ma 'kota' a kot ma kompilator") # inny sposób

# definiowanie stringów na wiele linijek
print('''
ala 
ma
kota''')
# lub
print("""
kot
ma
kompilator""")

# OPERATORY PORÓWNIANA
print()
print(1 == 1) # równa się
print(1 != 1) # nie równa się
print(1 > 2)
print(1 < 2)

# INSTRUKCJA WARUNKOWA IF

# PĘTLA WHILE
i = 0

print()