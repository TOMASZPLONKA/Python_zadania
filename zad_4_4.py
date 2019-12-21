#-- DO ŚCIĄGNIĘCIA

"""
# Zadanie #4
Zaimplementuj klasę `Basket` umożliwiającą dodawanie produktów w określonej liczbie do koszyka.
Zaimplementuj metodę obliczającą całkowitą wartość koszyka oraz wypisującą informację o zawartości koszyka.
Dodanie dwa razy tego samego produktu do koszyka powinno stworzyć tylko jedną pozycję.
Przykład użycia:
basket = Basket()
product = Product(1, 'Woda', 10.00)
basket.add_product(product, 5)
basket.count_total_price()
50.0
basket.generate_report()
'Produkty w koszyku:\n
- Woda (1), cena: 10.00 x 5\n
W sumie: 50.00'
"""


class Produkt:
    def __init__(self,ID,nazwa,cena):
        self.ID = ID
        self.nazwa = nazwa
        self.cena = cena

    def __str__(self):
        return print(f'Za {self.nazwa} zapłacisz {self.cena} zł')


class Basket:
    def __init__(self):
        self.zawartosc = []

    def add_product(self, p: Produkt, ilosc: int = 1):
        for s in self.zawartosc:
            if s["produkt"].ID == p.ID:
                s["ilosc"] += ilosc
                return
        slownik = {"produkt": p, "ilosc":ilosc}
        self.zawartosc.append(slownik)


    def count_total_price(self):
        suma = 0
        for slow in self.zawartosc:
            suma += slow["produkt"].cena * slow["ilosc"]
        return suma
        # lub return sum(p.cena for p in zawartosc) to samo w 1 linijce

    def generate_report(self):
        for produkt in self.zawartosc:
            return print(f'Za {produkt.nazwa} zapłacisz {produkt.cena * ilosc} zł')




p1 = Produkt(15,'kawa',10)
p2 = Produkt(20,'herbata',5)
p3 = Produkt(25,'mięta',2)

b = Basket()
b.add_product(p1,5)
b.add_product(p2,2)
b.add_product(p2,1)
b.add_product(p3,1)

print(b.zawartosc)

print(b.count_total_price())
# print
print(p1)
print(str(p1))
print(p1.__str__(p2))

print("Produkt",{p1})








