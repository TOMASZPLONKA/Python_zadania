"""
### Zadanie 1.9 FizzBuzz
​
Napisz program, który wyświetla liczby od 1 do 100. Dla liczb podzielnych przez 3 niech program wyświetli `Fizz`;
dla liczb podzielnych przez 5 niech wyświetli `Buzz`; a dla liczb podzielnych przez 15 niech wyświetli `FizzBuzz`.
​
"""
licznik = 1
while licznik <= 100:
   if licznik % 3 == 0 and licznik % 5 != 0:
       print(f'{licznik} Fizz')
   elif licznik % 5 == 0 and licznik % 3 != 0:
       print(f'{licznik} Buzz')
   elif licznik % 15 == 0:
       print(f'{licznik} FizzBuzz')
   else:
       print(f'{licznik}')
   licznik = licznik + 1
