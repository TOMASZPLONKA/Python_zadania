"""
"# Zadanie #3
Zaimplementuj klasę `ElectricCar` odwzorowującą zachowanie samochodu elektrycznego. Klasa powinna umożliwiać pokonanie zadanego dystansu,
który nie może przekroczyć maksymalnego zasięgu zdefiniowanego dla samochodu. Samochód powinien mieć także możliwość naładowania baterii.
car = ElectricCar(100)
car.drive(70)
70
car.drive(50)
30
car.drive(50)
0
car.charge()
car.drive(50)
50
"""
class ElectricCar:
    def __init__(self,samochod,dystans):
        self.samochod = samochod
        self.dystans = dystans
        self.zasieg = self.dystans


    def car_drive(self,ile_kilometrow):
        if self.dystans - ile_kilometrow >=0:
            self.dystans -= ile_kilometrow
            return ile_kilometrow
        else:
            ile_kilometrow = self.dystans
            self.dystans -= ile_kilometrow
            return ile_kilometrow

    def car_charge(self):
        self.dystans = self.zasieg


x = ElectricCar('Prius', 200)
print(f'Przejedziesz {x.car_drive(15)} km')
print(f'Przejedziesz {x.car_drive(305)} km')
print(f'Przejedziesz {x.car_drive(605)} km')
x.car_charge()
print(f'Przejedziesz {x.car_drive(400)} km')
x.car_charge()
print(f'Przejedziesz {x.car_drive(800)} km')