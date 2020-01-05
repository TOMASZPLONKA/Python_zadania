with open("emails.txt") as plik:
    wiersze = plik.readlines()

zbior = set()
# zbior = {wiersz.strip().lower() for wiersz in wiersze if wiersz.count("@") == 1} - skrócony zapis tego co zostało rozpisane w liniach 7-10

for wiersz in wiersze:
    napis = wiersz.strip().lower()
    if napis.count("@") == 1:
        zbior.add(napis)

with open("clean_emails.txt",mode = 'w') as plik:
    for email in sorted(zbior):
        plik.write(email)
        plik.write("\n")
