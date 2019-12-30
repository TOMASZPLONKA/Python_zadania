"""
# Zadanie #12
Zaimplementuj klasy odpowiedzialne za różne typy promocji - opartą o stałą wartość i procent od wartości.
Promocje można dodawać do koszyka. Koszyk może mieć aktywnych wiele promocji.
Pamiętaj o obsłużeniu przypadku gdy wartość koszyka spadnie poniżej zera.
Przykład użycia:
basket = Basket()
discount = ValueDiscount(10.0)
basket.add_discount(discount)
"""


class Product:
    def __init__(self, id, nazwa, cena):
        self.id = id
        self.nazwa = nazwa
        self.cena = cena

    def print_info(self):
        print(f"{self.nazwa}, ID: {self.id}, Cena: {self.cena} PLN")

    def __str__(self):
        return f"Nazwa: {self.nazwa}, ID: {self.id}, Cena: {self.cena} PLN"

    def __repr__(self):
        return f"<Product ID: {self.id}>"


class Basket:
    def __init__(self):
        self.zawartosc = []

    def add_product(self, p: Product, ilosc: int = 1):
        for s in self.zawartosc:
            if s["produkt"] == p:
                s["ilosc"] += ilosc
                return
        # jeśli tu dojdziemy to znaczy, ze na liscie nie ma jeszcze takiego produktu
        slownik = {"produkt": p, "ilosc": ilosc}
        self.zawartosc.append(slownik)

    def count_total_price(self):
        suma = 0
        for slow in self.zawartosc:
            suma += (slow["produkt"].cena) * slow["ilosc"]
        return round(suma,2)


class Discount:
    def __init__(self):
        self.promocje = []

    def discount(self, p: Product, param: int = 0):
        value = 0
        for i in b.zawartosc:
            if i["produkt"] == p:
                method = input(f'Podaj rodzaj promocji produktu {p.nazwa} (B = Brak, P = Procentowa, K = Kwotowa) ')
                while method != "B" and method != "P" and method != "K":
                    method = input(f'Podaj prawidłowy rodzaj promocji produktu {p.nazwa} (B = Brak, P = Procentowa, K = Kwotowa) ')
                    break
                if method == 'B':
                    slownik1 = {"produkt": p, "metoda": method, "param": param, "value": value}
                    self.promocje.append(slownik1)
                    return value
                elif method == 'P':
                    param = int(input("Podaj procent obniżki: "))
                    slownik1 = {"produkt": p, "metoda": method, "param": param, "value": value}
                    self.promocje.append(slownik1)
                    for i in d.promocje:
                        if i["produkt"] == p:
                            if i["param"] < 70:  # maksymalna promocja 70 %
                                value = round(i["produkt"].cena * i["param"] / 100, 2)
                                slownik1['value'] = value
                            else:
                                value = round(i["produkt"].cena * 0.7, 2)
                                slownik1['value'] = value
                            return value
                elif method == 'K':
                    param = float(input("Podaj kwotę obniżki: "))
                    slownik1 = {"produkt": p, "metoda": method, "param": param, "value": value}
                    self.promocje.append(slownik1)
                    for i in d.promocje:
                        if i["produkt"] == p:
                            if i["param"] < i["produkt"].cena * 0.7:  # maksymalna promocja 70 %
                                value = i["param"]
                                slownik1['value'] = value
                            else:
                                value = round(i["produkt"].cena * 0.7, 2)
                                slownik1['value'] = value
                            return value


    def add_discount(self):
        total = b.count_total_price()
        self.zawartosc = b.zawartosc
        for l in self.zawartosc:
            total = total - (d.discount(l["produkt"]) * l["ilosc"])
        return round(total,2)


p1 = Product(1, "Woda", 2.99)
p2 = Product(2, "Cola", 5.99)
p3 = Product(3, "Piwo", 3.15)
b = Basket()
b.add_product(p1)
b.add_product(p2, 15)
b.add_product(p1)
b.add_product(p3,5)
print(b.zawartosc)
print(p1)
print(p2)
print(p3)
d = Discount()
print(f'Rachunek przed uwzględnieniem promocji: {b.count_total_price()}')
print(f'Rachunek po uwzględnieniu promocji: {d.add_discount()}')
print(f'Kwota promocji: {d.discount(p1)}')
print(f'Kwota promocji: {d.discount(p2)}')
print(d.promocje)
