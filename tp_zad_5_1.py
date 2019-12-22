"""
# Zadanie #1
Zaimplementuj iterator odliczający od 0 do zadanego limitu.
Przykładowe użycie:
for number in Counter(10):
"""

class Counter:
    def __init__(self,limit):
        self.limit = limit

    def __iter__(self):
        self.i = 1
        return self

    def __next__(self):
        if self.i > self.limit:
            raise StopIteration
        wynik = self.i
        self.i +=1
        return wynik

number = Counter(8)
for i in number:
    print(i)