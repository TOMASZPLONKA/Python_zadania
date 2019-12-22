class Vowels:
    def __init__(self,napis):
        self.napis = napis
        self.limit = len(napis)


    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index > self.limit:
            raise StopIteration
        for char in napis:
            if char in ('a','e','i','o','u','y'):
                return char

for x in Vowels('ala ma kota'):
    print(x)