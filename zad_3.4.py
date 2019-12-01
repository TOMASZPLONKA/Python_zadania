"""Zaimplementuj funkcję formatującą podane napisy.
Przykład użycia:
formatuj(
    'koszt $cena PLN',
    'kwota $cena brutto',
    cena=10,
)
'koszt 10 PLN\nkwota 10 brutto'"""

def formatuj(*args,**kwargs):
    rezultat =[]
    for napis in args:
        for nazwa_do_podmiany, wartosc in kwargs.items():
            napis = napis.replace(f'${nazwa_do_podmiany}',str(kwargs[nazwa_do_podmiany]))
        rezultat.append(napis)
    return '\n'.join(rezultat)

print( formatuj('koszt $cena PLN','kwota $cena brutto',cena = 10) )
print( formatuj('ala ma $co', co ='kota') )
print( formatuj('Nazywam się $imie $nazwisko', imie = 'Tomasz', nazwisko = 'Płonka'))

def wszystko():
    assert formatuj('Autor $imie $nazwisko','Czesc $imie $nazwisko', imie='Tomasz',nazwisko='Plonka') == 'Autor Tomasz Plonka\nCzesc Tomasz Plonka'


