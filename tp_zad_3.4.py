"""
Napisz dekorator `crazy_case`, który co drugą literę w słowie będzie zamieniał na dużą.
```python
@crazy_case
def powiedz_ala():
	return 'Ala ma kota'

print(powiedz_ala()) # aLa mA KoTa
"""
def log(funkcja_do_udekorowania):
    def wrapper(*args, **kwargs):
        wynik = funkcja_do_udekorowania(*args, **kwargs).lower()
        do_podmiany = (wynik[1::2])
            for i in wynik:
                if i

        wynik = wynik.replace(wynik[1::2], do_podmiany.upper())
        return wynik
    return wrapper

@log
def powiedz_ala():
	return 'Ala ma kota'

print( powiedz_ala() )
