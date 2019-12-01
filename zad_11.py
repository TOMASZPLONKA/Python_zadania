x = int(input("Podaj pozycję X: "))
y = int(input("Podaj pozycję Y: "))


if x > 0 and x <= 10: # lub 0 < x <= 10
    if y > 0 and y <= 10:
        print("Lewy dolny róg")
    elif y > 10 and y <= 90:
        print("Centrum")
    elif y > 90 and y <= 100:
        print("Prawy dolny róg")
    else:
        print("Poza planszą")
elif x > 10 and x <= 90:
    if y > 0 and y <= 10:
        print("Prawa krawędź")
    elif y > 10 and y <= 90:
        print("Centrum")
    elif y > 90 and y <= 100:
        print("Lewa krawędź")
    else:
        print("Poza planszą")
elif x > 90 and x <= 100:
    if y > 0 and y <= 10:
        print("Prawy dolny róg")
    elif y > 10 and y <= 90:
        print("Prawa krawędź")
    elif y > 90 and y <= 100:
        print("Prawy górny róg")
    else:
        print("Poza planszą")
else:
    print("Poza planszą")



