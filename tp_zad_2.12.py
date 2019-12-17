"""
Napisz program, który posortuje liczby w liście przy wykorzystaniu
algorytmu "sortowanie przez wybieranie".
"""
a = [5,-8,14,25,45,0,-5,10,20,5.5,100,6,-15,-25,18,32,58,71,-1,99]
print(a)

def selection_sort(y):
    for i, n in enumerate(y):
        j, m = min(enumerate(y[i:]), key = lambda a: a[1])
        y[j + i], y[i] = n, m
    return y
print(selection_sort([5,-8,14,25,45,0,-5,10,20,5.5,100,6,-15,-25,18,32,58,71,-1,99]))





