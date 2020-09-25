# Кегельбан

nb = []
nk = input()                                # вводим количество кеглей (n) и шаров (k)
n, k = [int(n) for n in nk.split()]

for j in range(n):                          # по количеству кеглей заполняем пустой список
    nb.append('I')

for i in range(k):                          # по количеству запущенных шаров
    lr = input()                            # вводим диапазоны сбитых кегель
    l, r = [int(n) for n in lr.split()]     # l - левая граница, r - правая граница
    for s in range(l - 1, r, 1):            # заменяем сбитые кегли точками (.)
        nb[s] = '.'

print(''.join(nb))