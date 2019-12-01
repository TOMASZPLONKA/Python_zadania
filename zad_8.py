wymiar_a = int(input("Podaj wymiar a w cm: "))
wymiar_b = int(input("Podaj wymiar b w cm: "))
wymiar_c = int(input("Podaj wymiar c w cm: "))

objetosc = wymiar_a  * wymiar_b * wymiar_c

print(f' Objętość opakowania jest większa od 1 litra: {objetosc > 1000}')