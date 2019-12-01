liczby= [-5, -10, 6, -11, 1, 0, 8, -2, -4, -6]

liczba_dodatnich = 0
liczba_ujemnych = 0

for element in liczby: # dla każdego elementu listy liczby
    if element <0:
        liczba_ujemnych += 1
    elif element >0:
        liczba_dodatnich += 1

print(f'Liczb ujemnych = {liczba_ujemnych}')
print(f'Liczb dodatnich = {liczba_dodatnich}')

