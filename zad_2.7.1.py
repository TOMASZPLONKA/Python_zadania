napis = input("Podaj napis: ")
samogloski = ['a','e','i','o','u'] # lista
samogloski = ('a','e','i','o','u') # tupla
samogloski = 'aeiou' # ciąg znaków - też zadziała
ile_samoglosek = 0

for samogloska in samogloski:
    ile_samoglosek += napis.lower().count(samogloska)
print(f'Liczba samogłosek w podanym napisie: {ile_samoglosek} ')