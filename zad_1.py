"""
Napisz funkcję sprawdzającą, czy dane liczba jest liczbą pierwszą.
Przykład użycia:
czy_jest_pierwsza(10)
False
czy_jest_pierwsza(17)
True
"""
def czy_jest_pierwsza(liczba: int) -> bool:
    """
    Funkcja sprawdza czy liczba jest podzielna przez 1 i samą siebie. Dodatkowo musi być większa od 1.
    :param liczba:
    :return:
    """
    if liczba <= 1 or type(liczba) is not int:
        return False
    for i in range(2, liczba):
        if liczba % i == 0:
            return False
    return True # uwaga na poziom wcięcia


print(czy_jest_pierwsza(10))
print(czy_jest_pierwsza(11))
print(czy_jest_pierwsza(47))
print(czy_jest_pierwsza(95))

# funkcja do testowania, musi się zaczynać od test_
def test_czy_liczba_pierwsza():
    liczba = 5
    wynik = czy_jest_pierwsza(liczba)
    assert wynik == True

# żeby uruchomić funkcję testową - skrót Alt+Shift+F10

def test_liczb_pierwszych():
    assert czy_jest_pierwsza(5) == True
    assert czy_jest_pierwsza(11)
    assert czy_jest_pierwsza(13) is True

def test_liczb_nie_pierwszych():
    assert czy_jest_pierwsza(1) == False
    assert czy_jest_pierwsza(4) == False
    assert czy_jest_pierwsza(-1) == False
    assert czy_jest_pierwsza(9) == False

