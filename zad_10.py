"""
Napisz program zliczający liczbę wystąpień każdego znaku w
podanym przez użytkownika napisie.
"""

napis = input("Podaj napis do zliczenia liczby znaków: ")
wystapienia = {}
"""
for znak in napis:
    if znak not in wystapienia:
        wystapienia[znak] = 1
    else:
        wystapienia[znak] +=1
print(wystapienia)
"""
### drugi sposób

for znak in napis:
    if znak not in wystapienia:
        wystapienia[znak] = 0
    wystapienia[znak] +=1
print(wystapienia)

print()

# sorted() sortuje listę tupli po pierwszym elemencie tupli, czyli po kluczu słownika
for litera, liczba_wystapien in sorted(wystapienia.items()):
    print(f'{litera} = {liczba_wystapien}')
