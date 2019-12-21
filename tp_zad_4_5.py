"""
Zaimplementuj klasę `CashMachine` umożliwiającą wpłacanie i wypłacanie pieniędzy. Zadbaj o to aby stan bankomatu przetrzymywany był w zmiennych prywatnych.
Przykład użycia:
cash_machine = CashMachine()
cash_machine.is_available()
False
cash_machine.put_money([200, 100, 100, 50])
cash_machine.is_available()
True
cash_machine.withdraw_money(150)
[100, 50]

"""

class CashMachine:
    def __init__(self):
        self.zawartosc =[]


    def is_available(self):
        return bool(self.zawartosc)

    def put_money(self, banknoty):
        self.zawartosc.extend(banknoty)
        #for b in banknoty:
            #self.zawartosc.append(b) to samo

    def withdraw_money(self, ile):
        wynik = []
        for b in self.zawartosc:
            if b <= ile:
                wynik.append(b)
                ile-= b

        if ile != 0:
             return []
        for banknot in wynik:
             self.zawartosc.remove(banknot)
        print(f'Na koncie pozostało: {self.zawartosc}')
        print(f'Wypłata: {wynik}')
        return wynik

bankomat = CashMachine()

bankomat.put_money([200, 100, 100, 50])
bankomat.is_available()
bankomat.withdraw_money(150)
bankomat.withdraw_money(150)