"""
# Zadanie 5
Napisz program znajdujący w dostarczonym pliku wszystkie wystąpienia:- kodów pocztowych - `12-123`
- adresów email - `test@email.com`
- dat - `12 Jan 1990`Skorzystaj z modułu `re`.
"""
import re
kod_pocztowy = re.compile(r"[0-9][0-9]-[0-9][0-9][0-9]") # lub \b\d{2}-\d{3}
date = re.compile(r"\b\d{2} [A-Z][a-z]{2} \d{4}\b")
adres = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

with open ("regex.txt") as plik:
    napis = plik.read()

kod = kod_pocztowy.findall(napis)
data = date.findall(napis)
email = adres.findall(napis)
print(kod)
print(data)
print(email)

