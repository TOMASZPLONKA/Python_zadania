"""
ważne biblioteki:

JSON - uniwersalny format zapisu danych do przekazywania między aplikacjami
json.load() - do operowania na plikach
json.loads() - do operowania na napisach
json.dump() - do operowania na plikach
json.dumps() - do operowania na napisach
pusty napis nie zostanie przetworzony przez json
"""
import json
obiekt = {"imie": "Jan", "nazwisko": "Nowak", "cos": [None,1,2,3]}
napis = json.dumps(obiekt)
print(napis)
print(type(napis))
print(repr(napis))
print(30*'-')
wynik = json.loads(napis)
print(type(wynik))
print(wynik)

with open("test.json") as plik:
    obiekt = json.load(plik)
print(obiekt)
obiekt.append(123)

with open("test.json","w") as plik:
    json.dump(obiekt,plik)

# import do ściągania stron http
from urllib.request import urlopen
with urlopen("http://api.nbp.pl/api/cenyzlota?format=json") as plik:
    napis = plik.read().decode('utf-8')

print(napis)
print(type(napis))


"""
Biblioteka tkinter - tworzenie obiektów

"""

import tkinter as tk
def fun():
    print(entry.get())
    napis = entry.get()
    label.configure(text=napis) # przestawienie dowolnego parametru danego obiektu

root = tk.Tk()

przycisk = tk.Button(master=root, text= "Click me!",command= fun)
# atrybut master w nim definiujemy, gdzie Button ma się wyświetlić (w tym wypadku w obiekcie root)
# command - atrybut, który przekazuje funkcję - bez nawiasów, bo ma ją przekazać, a nie wywołać
przycisk.grid(row=0, column = 0) # metoda grid określa gdzie obiekt ma się pojawić, są też inne metody
przycisk2 = tk.Button(master=root, text= "Click me 2!")
przycisk2.grid(row=0, column = 1)
label = tk.Label(master = root, text = "Przykładowy tekst")
label.grid(row=1, column=0)
entry = tk.Entry(master=root)
entry.grid(row=1,column=1)
# przy rozciąganiu - określenie w jaki sposób ma się odbywać rozciąganie, w tym wypadku 2 kolumna rozciąga się 2 razy bardziej
root.columnconfigure(0,weight = 0)
root.columnconfigure(1,weight = 1)

root.title("Moje pierwsze okienko")
root.mainloop()

"""
Jeżeli tworzymy okienka często trzeba dodać interpreter, np. py2.exe

strona internetowa - regex.com - informacje o pythonie, można szukać np. jak skonstruować wyrażenia regularne
"""

# moduł re - regular expression

import re
wyrazenie = re.compile(r"ab*c") # litera "r" powoduje, że python nie traktuje jakichś szczególnych znaków (np."\") jako znaków specjalnych, tylko tekst
with open ("regex.txt") as plik:
    napis = plik.read()

print(wyrazenie)

wynik = wyrazenie.findall(napis)
print(wynik)

import turtle

licznik = 80

bogdan = turtle.Turtle()
while True:
    bogdan.forward(50)
    bogdan.right(licznik)
    bogdan.forward(50)
turtle.done()

bogdan.done