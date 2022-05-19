from itertools import dropwhile, filterfalse, takewhile, repeat

print(list(dropwhile(lambda x: x < 5, [1, 4, 5, 4, 1])))  # tira da lista até chegar na condição falsa.
print(list(filterfalse(lambda x: x % 2, range(10))))  # tira da lista tudo da condição falsa
print(list(takewhile(lambda x: x < 5, [1, 4, 5, 4, 1])))  # contrário do dropwhile.
print(list(repeat('x', 3)))
