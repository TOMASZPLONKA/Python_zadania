def generator():
    yield 3
    yield 5
    yield 7
# kluczowe słowo yield, zwracany generator object, następne wywołanie będzie od kolejnej zmiennej (działa jak iterator)

# print(generator())

for i in generator():
    print(i)
"""
it = iter(generator())
print(next(it))
print(next(it))
print(next(it))
"""
print(60*'-')

def nasz_range(x):
    i = 0
    while i < x:
        yield i
        i += 1

for i in nasz_range(5):
    print(i)

print(60 * '-')

def nasz_range2(x):
    for i in range(x):
        yield i

for i in nasz_range2(2):
    print(i)

print(60 * '-')