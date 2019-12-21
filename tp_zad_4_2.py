"""
# Zadanie #2
Zaimplementuj klasę `Employee` umożliwiającą rejestrowanie czasu pracy oraz wypłacanie pensji na podstawie zadanej stawki godzinowej. Jeżeli pracownik będzie pracował więcej niż 8 godzin (podczas pojedynczej rejestracji czasu) to kolejne godziny policz jako nadgodziny (z podwójną stawką godzinową).
Przykład użycia:
 employee = Employee('Jan', 'Nowak', 100.0)
 employee.register_time(5)
 employee.pay_salary()
500.0
 employee.pay_salary()
0.0
 employee.register_time(10)
 employee.pay_salary()
1200.0
"""

class Employee:
    def __init__(self,imie,nazwisko,time,stawka):
        self.imie = imie
        self.nazwisko = nazwisko
        self.time = time
        self.stawka = stawka


    def pay_salary(self,time,stawka):
        self.time = time
        self.stawka = stawka
        if time <= 8:
            return time * stawka
        else:
            return (8*stawka) + (stawka*2 *(time-8))

x = Employee('Jan','Nowak',9,200)

print(x.pay_salary(x.time,x.stawka))





