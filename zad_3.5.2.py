""""
Ciąg Fibonacciego
n = 0 -> 0
n = 1 -> 1
n = 2 -> 1
n = 3 -> 2
n = 4 -> 3
n = 5 -> 5
n = 6 -> 8
n = 7 -> 13
...
"""
def fib (n:int) -> int:
    if n < 0 or type(n) is not int:
        # return None  mankament tego rozwiązania - programista używający tej funkcji będzie musiał sprawdzić czy nie dostał wartości None
        raise ValueError('n musi być intem i być większe lub równe 0')
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n-2)

print(fib(50))

import pytest
def test_ujmne():
    with pytest.raises(ValueError)

def test_fibonacci():
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3
    assert fib(5) == 5
    assert fib(6) == 8
    assert fib(7) == 13
    assert fib(8) == 21
    assert fib(9) == 34
    assert fib(10) == 55
    assert fib(15) == 610
