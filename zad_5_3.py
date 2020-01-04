def vowels(napis):
    i = 0
    while i < len(napis):
        znak = napis[i]
        if znak.lower() in ("aeiouy"):
            yield znak
        i += 1

for x in vowels("poniedziałek"):
    print(x)

print(60*"-")


def vowels(napis):
    for znak in napis:
        if znak.lower() in "aeiouy":
            yield znak

for x in vowels("Ala ma kota"):
    print(x)