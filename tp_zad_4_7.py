"""
# Zadanie #7
Zaimplementuj klasę `PremiumEmployee`, która będzie klasą pochodną `Employee`. Klasa ta powinna umożliwiać dodatkowo przyznawanie bonusów pracownikowi.
employee = PremiumEmployee('Jan', 'Nowak', 100.0)
employee.register_time(5)
employee.give_bonus(1000.0)
employee.pay_salary()
1500.0
"""

class Employee:
    def __init__(self,imie,nazwisko,stawka):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stawka = stawka
        self.przepracowany_czas = 0

    def register_time(self,ile):
        self.przepracowany_czas += ile
        if ile >8:
            self.przepracowany_czas += ile - 8

    def pay_salary(self):
        wyplata = self.przepracowany_czas * self.stawka
        self.przepracowany_czas = 0
        return wyplata

class PremiumEmployee(Employee):
    def __init__(self,imie,nazwisko,stawka):
        super().__init__(imie,nazwisko,stawka)
        self.bonus = 0

    def give_bonus(self,bonus):
        self.bonus = bonus

    def pay_salary(self):
        bonus = self.bonus
        self.bonus = 0
        return super().pay_salary() + bonus


p = PremiumEmployee('Jan', 'Nowak', 100.0)

p.register_time(5)
p.register_time(5)
print(f'Wypłata:', p.pay_salary())
print(f'Wypłata:', p.pay_salary())
p.register_time(10)
print(f'Wypłata:', p.pay_salary())
p.register_time(10)
p.give_bonus(1000.0)
print(f'Wypłata:', p.pay_salary())

