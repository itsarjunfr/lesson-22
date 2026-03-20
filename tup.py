tuplex = ('tuple', False, 3.2, 1)
print(tuplex)

tuplex = (1, 2, 3, 4, 5, 6, 7, 8)
print(tuplex)
tuplex = tuplex + (9,)
print(tuplex)

tuplex = (1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
print(tuplex.count(3))
print(tuplex[:-6:-1])