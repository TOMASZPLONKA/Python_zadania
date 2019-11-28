"""### Zadanie 1.2 | Buty do szewca (ok. 1 godz.)
​
Napisz taki program: użytkownik ma podać, w jaki dzień tygodnia oddał buty do szewca (poniedziałek to dzień 1,
wtorek to dzień 2 itp.). Ma też podać, ile dni będzie trwała naprawa.
​
Program ma wypisać, w jaki dzień tygodnia buty będą gotowe do odbioru. Jeśli tak będzie ci wygodniej, możesz założyć,
że naprawa butów nigdy nie będzie trwała dłużej niż siedem dni. """

## 1 wersja - dzień tygodnia podany w formie liczby

dzien_tygodnia = int(input('Podaj dzień tygodnia, w którym oddałeś buty: '))
if dzien_tygodnia == 7:
    print('W niedzielę szewc nie pracuje')
    dzien_tygodnia = int(input('Podaj dzień tygodnia, w którym oddałeś buty: '))

liczba_dni = int(input('Podaj ile dni będzie trwała naprawa: '))
wynik = (dzien_tygodnia + liczba_dni) % 6 # założyłem, że w niedzielę szewc nie pracuje

if wynik == 1:
    print('Buty będą do odbioru w poniedziałek')
elif wynik == 2:
    print('Buty będą do odbioru we wtorek')
elif wynik == 3:
    print('Buty będą do odbioru w środę')
elif wynik == 4:
    print('Buty będą do odbioru w czwartek')
elif wynik == 5:
    print('Buty będą do odbioru w piątek')
else:
    print('Buty będą do odbioru w sobotę')



## 2 wersja - dzień tygodnia podany słownie

dane_wejsciowe = input('Podaj dzień tygodnia, w którym oddałeś buty: ')

if dane_wejsciowe == 'poniedziałek':
    dzien_tygodnia = 1
elif dane_wejsciowe == 'wtorek':
    dzien_tygodnia = 2
elif dane_wejsciowe == 'środa':
    dzien_tygodnia = 3
elif dane_wejsciowe == 'czwartek':
    dzien_tygodnia = 4
elif dane_wejsciowe == 'piątek':
    dzien_tygodnia = 5
elif dane_wejsciowe == 'sobota':
    dzien_tygodnia = 6
elif dane_wejsciowe == 'niedziela':
    print('W niedzielę szewc nie pracuje')
    input('Podaj dzień tygodnia, w którym oddałeś buty: ')

liczba_dni = int(input('Podaj ile dni będzie trwała naprawa: '))
wynik = (dzien_tygodnia + liczba_dni) % 6 # założyłem, że w niedzielę szewc nie pracuje

if wynik == 1:
    print('Buty będą do odbioru w poniedziałek')
elif wynik == 2:
    print('Buty będą do odbioru we wtorek')
elif wynik == 3:
    print('Buty będą do odbioru w środę')
elif wynik == 4:
    print('Buty będą do odbioru w czwartek')
elif wynik == 5:
    print('Buty będą do odbioru w piątek')
else:
    print('Buty będą do odbioru w sobotę')


