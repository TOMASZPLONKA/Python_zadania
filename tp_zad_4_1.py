"""
Zaimplementuj klasę `Product` przechowującą informację o cenie, nazwie oraz ID produktu. Zaimplementuj metodę wypisującą informację o produkcie na konsolę.
Przykład użycia:
product = Product(1, 'Woda', 10.99)
Produkt "Woda", id: 1, cena: 10.99 PLN
"""

class Produkt:
    def __init__(self,ID,nazwa,cena):
        self.ID = ID
        self.nazwa = nazwa
        self.cena = cena

    def informacja(self):
        print(f'ID: {self.ID}, nazwa: {self.nazwa}, cena: {self.cena} zł')

x = Produkt(15,'kawa',10)
y = Produkt(20,'herbata',5)
z = Produkt(25,'mięta',2)

x.informacja()
y.informacja()
z.informacja()

print(x.nazwa)