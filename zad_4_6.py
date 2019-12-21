"""
# Zadanie #6
Zaimplementuj klasę `Vector` dostarczającą funkcjonalność wektora swobodnego na dwuwymiarowej płaszczyźnie.
Wektory powinny mieć możliwość dodawania, odejmowania, mnożenia (przez liczbę), porównywania (po długości) oraz powinny posiadać czytelną reprezentację napisową.
Przykład użycia:
vector_1 = Vector(x=1, y=2)
vector_2 = Vector(x=1, y=2)
vector_3 = vector_1 + vector_2
"""

class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"[{self.x}, {self.y}]"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __
        pass

    def __lt__(self, other):
        pass


v1 = Vector(1, 2)
v2 = Vector(2, 3)

print(v1)
print(v2)

v3 = v1 + v2
print(v3)
print(f'{v1} + {v2} = {v3}')
v1 * 3
3 * v1