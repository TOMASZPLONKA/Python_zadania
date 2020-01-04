"""
Zadanie  3
Napisz program wczytujący listę adresów email z pliku i tworzący nowy plik z odfiltrowaną zawartością.
Wejściowy plik może zawierać duplikaty adresów, ten sam adres pisany różną wielkością liter, linie zawierające białe znaki oraz
błędne adresy email (brak znaku `@` lub występuje on wiele razy). Wynikowy plik powinien zawierać unikalne, posortowane, poprawne adresy email.
Przykład użycia:$ python clean_emails.py emails.txt cleaned_emails.txt"
"""

with open("emails.txt") as plik:
    wiersze = plik.read().split()
    emails = {}

for nr, wiersz in enumerate(wiersze):
    lista = wiersz.lower()
    if lista not in emails:
       emails[lista] = 0
    emails[lista] = nr

def licz_znaki(napis):
    if napis.count('@') == 1:
        return True
    else:
        return False

#if not os.path.isfile(new_emails):
new_emails = open('new_emails', 'w')
for v in sorted(emails):
    if licz_znaki(v) is True:
        new_emails.write(v)
        new_emails.write(";\n")
new_emails.close()

