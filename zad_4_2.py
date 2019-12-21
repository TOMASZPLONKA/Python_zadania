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

p = Employee("Jan","Nowak", 100)
p.register_time(5)
p.register_time(5)
print(f'Wypłata:', p.pay_salary())
print(f'Wypłata:', p.pay_salary())
p.register_time(10)
print(f'Wypłata:', p.pay_salary())