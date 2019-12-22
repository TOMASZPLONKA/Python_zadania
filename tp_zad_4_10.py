"""
# Zadanie #10
Zaimplementuj mechanizm automatycznego generowania kolejnych ID dla produktów. Informację o kolejnym ID przechowuj jako pole klasowe.
Przykład użycia:
product_1 = Product('Woda', 1.99)
product_1.id
1
product_2 = Product('Chleb', 2.50)
product_2.id
2

"""
class Product:
    POLE_KLASOWE = 1

    def __init__(self, nazwa, cena):
        self.id = Product.POLE_KLASOWE
        Product.POLE_KLASOWE +=1
        self.nazwa = nazwa
        self.cena = cena

    def print_info(self):
        print(f"{self.nazwa}, ID: {self.id}, Cena: {self.cena} PLN")

    def __str__(self):
        return f"ID: {self.id}, Nazwa: {self.nazwa}, Cena: {self.cena} PLN"

    def __repr__(self):
        return f"<Product ID: {self.id}>"

class Basket:
    def __init__(self):
        self.zawartosc = []

    def add_product(self, p: Product, ilosc: int = 1):
        for s in self.zawartosc:
            if s["produkt"].id == p.id:
                s["ilosc"] += ilosc
                return
        # jeśli tu dojdziemy to znaczy, ze na liscie nie ma jeszcze takiego produktu
        slownik = {"produkt": p, "ilosc": ilosc}
        self.zawartosc.append(slownik)

    def count_total_price(self):
        suma = 0
        for slow in self.zawartosc:
            suma += slow["produkt"].cena * slow["ilosc"]
        return suma

p1 = Product("Woda", 10.99)
p2 = Product("Cola", 5.99)
p3 = Product("Sok", 7.99)
x = [Product("Woda", 10.99) for _ in range(100)]
print(p1)
print(p2)
print(p3)
print(x)