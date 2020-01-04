def czy_jest_pierwsza(liczba: int):
    if liczba <= 1 or type(liczba) is not int:
        return False
    for i in range(2, liczba):
        if liczba % i == 0:
            return False
    return True

def liczby_pierwsze (liczba):
    i = 0
    while i <= liczba:
        if czy_jest_pierwsza(i) is True:
            yield i
        i += 1

for x in liczby_pierwsze(100):
    print(x)

