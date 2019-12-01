"""
Zaimplementuj funkcję spłaszczającą podaną listę.
Przykład użycia:
splaszcz([1, 2, 3, [4, 5, [6]], 7])
[1, 2, 3, 4, 5, 6, 7]
"""

def splaszcz(lista: list): -> list:
    if type(lista) is not lista:
       raise TypeError('Musisz podać listę'')

    wynik = lista()

    for element in lista:
        if type(element) is list:
            wynik += splaszcz(element)
        else:
            wynik.append(element)

    return wynik

import pytest

def test_inne_typy():
    with pytest.raises(TypeError):
        splaszcz('ala ma kota')

def test_pusta_lista():
   assert splaszcz([]) == []

def test_splaszcz():
    assert splaszcz([1, 2, 3]) == [1, 2, 3]
    assert splaszcz([1, 2, [3, 4]]) == [1, 2, 3, 4]
    assert splaszcz([1, 2, 3, [4, 5, [6]], 7]) == [1, 2, 3, 4, 5, 6, 7]
    assert splaszcz([[1], [[2], [3, [4]], 5], 6, [7]]) == [1, 2, 3, 4, 5, 6, 7]