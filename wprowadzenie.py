"""
f = open("plik.txt")
napis = f.read()
print(f.read())
f.close()
print(repr(napis))
print(f.readlines())
for x in f:
    print(x)
"""

with open("plik.txt") as plik:
    print(plik.read())

