class Counter:
    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        return Counter_iterator(self)
    # nie musi być __next__(), bo zwraca inną klasę, w której jest metoda __next__()

class Counter_iterator:
    def __init__(self, counter):
        self.counter = counter
        self.x = 0

    # nie musi być __iter__(), bo jest w klasie, do której będzie zwracana metoda __next__()

    def __next__(self):
        if self.x < self.counter.limit:
            wynik = self.x
            self.x += 1
            return wynik
        raise StopIteration

i = Counter(3)

for x in i:
    print(f"{x} ", end="")
    for y in i:
        print(f"{y} ", end="")
    print()


