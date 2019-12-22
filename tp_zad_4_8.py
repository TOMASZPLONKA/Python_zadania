"""
# Zadanie #8
Zaimplementuj w klasie `CashMachine` rzucanie wyjątków w następujących przypadkach:
- brak miejsca na banknoty (ustal limit banknotów w bankomacie)
- zła wartość wypłacanej sumy (musi być podzielna przez 10)
- brak odpowiednich banknotów w bankomacie
Zaimplementuj prosty interfejs tekstowy do klasy bankomat obsługujący wszystkie wyjątki. Obsłuż także wyjątki wynikające z podania złych danych przez użytkownika.
Przykład użycia:
Podaj typ operacji: WYPŁATA
Podaj kwotę do wypłacenia: 150
BŁĄD: brak wystarczającej liczby banknotów dla kwoty 150!
"""

class CashMachineException(Exception):
    pass

class CashMachine:
    def __init__(self, limit = 10):
        self.__zawartosc =[]
        self.limit = limit

    def is_available(self):
        return len(self.__zawartosc) > 0

    def put_money(self, banknoty):
        if len(self.__zawartosc) + len(banknoty) > self.limit:
            raise CashMachineException(f"Przekroczono liczbę banknotów")
        self.__zawartosc.extend(banknoty)

    def withdraw_money(self, ile):
        if ile % 10 != 0:
            raise CashMachineException(f"Kwota {kwota} nie jest podzielna przez 10")
        kwota = ile
        wynik = []
        for b in self.__zawartosc:
            if b <= ile:
                wynik.append(b)
                ile-= b

        if ile != 0:
             raise CashMachineException(f"Brak odpowiednich banknotów do wypłacenia kwoty {kwota}")

        for b in wynik:
             self.__zawartosc.remove(banknot)

        return wynik

bankomat = CashMachine()
bankomat.put_money([200, 100, 100, 50, 200, 100, 100, 50, 200, 100])
while True:
    op = input ("Podaj rodzaj operacji [WPŁATA, WYPŁATA, KONIEC]: ")
    if op == "KONIEC":
        break
    elif op == "WYPŁATA":
        try:
            kwota = int(input("Podaj kwotę do wypłacenia: "))
            print(bankomat.withdraw_money(kwota))
        except CashMachineException as e:
            print(f"BŁĄD: {e}")
        except ValueError:
            print("Podaj liczbę! ")
    elif op == "WPŁATA":
        try:
            lista = input("Podaj banknoty oddzielone spacjami: ").split(" ")
            bankomat.put_money(list(map(int, lista)))
        except CashMachineException as e:
            print(f"BŁĄD: {e}")


