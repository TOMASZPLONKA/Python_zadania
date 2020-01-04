"""
# Zadanie 1Napisz program wypisujący na konsolę zawartość wskazanego pliku wraz z numerami linii. Obsłuż sytuację, gdy użytkownik nie poda nazwy pliku lub poda błędną nazwę.Przykład użycia:$ python test.txt
1: pierwsza linia pliku
2: druga linia pliku

"""
nazwa = input("Podaj nazwę pliku: ") #nazwa pliku albo pełna ścieżka

while True:
    try:
        with open(nazwa, encoding="utf-8") as plik: # encoding - kodowanie pliku, domyślnie na Windowsie cp1250, polskie znaki generalnie na UTF-8
            for nr, linia in enumerate(plik, 1):
                print(f'{nr:5}: {linia}', end='')
        break
    except FileNotFoundError:
        print("Nie ma takiego pliku")



