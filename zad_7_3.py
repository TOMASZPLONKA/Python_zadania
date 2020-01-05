"""
# Zadanie 3
Napisz program z graficznym interfejsem użytkownika (GUI) do obliczania kosztów przejazdu na zadanym dystansie
 na podstawie spalania samochodu oraz ceny paliwa. Skorzystaj z modułu `tkinter`.
"""

import tkinter as tk
def oblicz():
    dystans = float(entry1.get())
    spalanie = float(entry2.get())
    cena = float(entry3.get())
    wynik = dystans/100*spalanie*cena
    wynik_label4.configure(text = f"Koszt przejazdu = {wynik:.2f} PLN")
    return wynik
root = tk.Tk()

przycisk = tk.Button(master=root, text= "Oblicz",command= oblicz)
przycisk.grid(row=15, column = 15)
label1 = tk.Label(master = root, text = "Podaj dystans w km: ")
label1.grid(row=1, column=0,sticky=tk.W)
label2 = tk.Label(master = root, text = "Podaj średnie spalanie na 100 km: ")
label2.grid(row=2, column=0,sticky=tk.W)
label3 = tk.Label(master = root, text = "Podaj cenę paliwa w zł: ")
label3.grid(row=3, column=0,sticky=tk.W)
entry1 = tk.Entry(master=root)
entry1.grid(row=1,column=1)
entry2 = tk.Entry(master=root)
entry2.grid(row=2,column=1)
entry3 = tk.Entry(master=root)
entry3.grid(row=3,column=1)
wynik_label4 = tk.Label(master=root, text = '')
wynik_label4.grid(row=16,column=15)


root.title("Kalkulator, cena przejazdu")
root.mainloop()