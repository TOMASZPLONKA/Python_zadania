class Vowels:
    def __init__(self,napis):
        self.napis = napis
        self.limit = len(napis)

    def __iter__(self):
        self.a = 0
        return self

    def __next__(self):
        while self.a < self.limit:
            x = self.napis[self.a]
            self.a += 1
            if x.lower() in ('a','e','i','o','u','y'):
                return x
        raise StopIteration

for x in Vowels('Ala ma kota'):
    print(x)