"""

"""


def policz_znaki(napis, start = '[', end = ']'):
    if napis.count(start) != 1 or napis.count(end) != 1:
        return 0
    return len(napis[napis.index(start) + 1 : napis.index(end)])


def test_policz_znaki_w_pustym_napisie():
    assert policz_znaki(napis='') == 0

def test_niepusty_napis_bez_znacznikow():
    assert policz_znaki('ala ma kota') == 0

def test_niepusty_napis_domylne_znaczniki():
    assert policz_znaki('ala ma [kota], a kot ma kompilator') == 4
def test_inny_start():
    assert policz_znaki('ala ma >kota], a kot ma kompilator', '>') == 4
def test_inny_poczatek_i_koniec():
    assert policz_znaki('ala ma !kota!, a kot ma kompilator', '!', '!') == 4
