napis = input("Podaj napis: ")
samogloski = ['a','e','i','o','u'] # lista
samogloski = ('a','e','i','o','u') # tupla
samogloski = 'aeiou' # ciąg znaków - też zadziała
ile_samoglosek = 0

for znak in napis.lower():
    if znak in samogloski:
        ile_samoglosek +=1
print(f'Liczba samogłosek w podanym napisie: {ile_samoglosek} ')
