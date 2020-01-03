class Vowels:
    def __init__(self,napis):
        self.napis = napis
        self.limit = len(napis)

    def __iter__(self):
        self.a = 0
        return self

    def __str__(self):
        return f"Napis: {self.napis}"

    def __next__(self):
        for x in self.napis:
            x = self.napis[self.a]
            self.a += 1
            if x in ('a','e','i','o','u','y'):
                return x
            if self.a == self.limit:
                raise StopIteration

for x in Vowels('poniedziałek'):
    print(x)
