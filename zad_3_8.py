"""
Zaimplementuj zestaw dekoratorów otaczających zwracany przez
funkcję napis tagami HTML (pogrubienie, podkreślenie,
przekreślenie):
Przykład użycia:
@bold
@italic
def foo(arg):
return f'To jest {arg}'
"""

def bold(funkcja_do_udekorowania):
    def wrapper(*args,**kwargs):
        wynik = funkcja_do_udekorowania(*args,**kwargs)
        return f'<strong> {wynik} </strong>'
    return wrapper
@bold

def foo(arg):
    return f'To jest {arg}'

print(foo('Ala'))


def italic(funkcja_do_udekorowania):
    def wrapper(*args,**kwargs):
        wynik = funkcja_do_udekorowania(*args,**kwargs)
        return f'<em> {wynik} </em>'
    return wrapper

@italic
def foo(arg):
    return f'To jest {arg}'

print(foo('Ela'))
