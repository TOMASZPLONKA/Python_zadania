"""a = 1 # liczba wierszy
g = 1 # liczba gwiazdek w wierszu
l = int(input("Podaj dodatnią liczbę całkowitą: ")) # wprowadzona liczba
for a in range(1, l+1):
    print(f'{g:{l}}')
    #z = '*'*g
    #print(z)
    #print(f'{z:{l}}')
    print(f'{g*"*":{l}}')
    #print(f'{(g*"*"):{l}}')
    g = g+2
print()
a = int(input("Podaj dodatnią liczbę całkowitą: ")) # wprowadzona liczba
for a in range(1, a+1):
    for b in range(1, a+1):
        print(f'{a*b} ', end='')
    print()"""

"""
a = 1 # liczba wierszy
g = [1]
l = int(input("Podaj dodatnią liczbę całkowitą: ")) # wprowadzona liczba
for a in range(1, l+1):
    print(f'{g[-1]:{l}}')
    g.append(g[-1]+2)
    print(g)

    #print(f'{(g*"*"):{l}}')

a = int(input("Podaj dodatnią liczbę całkowitą: ")) # wprowadzona liczba
g = 1
for a in range(1, a+1):
    for b in range(1, a+1):
        #print(f'{a*b:{3}}', end='')
        print(f'*', end='')
        g = g + 2
    print()
print()"""

"""
w = 1 # liczba wierszy
g = 1 # liczba gwiazdek w wierszu
l = int(input("Podaj dodatnią liczbę całkowitą: ")) # wprowadzona liczba
lista = list()
for w in range(1, l + 1):
    w = w + 1
    lista.append("*" * g)
    g = g + 2
print(lista)"""

w = 1 # liczba wierszy
g = 1 # liczba gwiazdek w wierszu
l = int(input("Podaj dodatnią liczbę całkowitą: ")) # wprowadzona liczba
z = None
for w in range(1, l + 1):
    w = w + 1
    z = ("*" * g)
    print("*" * g)
    g = g + 2


#print(f'{("*" * g):{lista.index[-1]}} ', end='')




