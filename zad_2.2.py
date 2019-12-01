liczby = list() # liczby = [] - tworzy pustą listę

while len(liczby) <= 10:
    liczba = int(input("Podaj liczbę: "))
    liczby.append(liczba)

print(liczby)
srednia = sum(liczby) / len(liczby)
print(srednia)


lista = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
i = 0
while i < len(lista):
    print(lista[i])
    i=+1

# PĘTLA FOR

for x in lista:
    print(x)