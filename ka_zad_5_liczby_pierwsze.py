def czy_jest_pierwsza(liczba: int):
    if liczba <= 1 or type(liczba) is not int:
        return False
    for i in range(2, liczba):
        if liczba % i == 0:
            return False
    return True

def liczby_pierwsze():
    num = 1
    while True:
        if czy_jest_pierwsza(num):
            yield num
        num += 1

for i, x in enumerate(liczby_pierwsze(),1):
    if x >=100:
        break
    print(f"{i}: {x}")