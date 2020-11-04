# вывод
world = input()

print(world[2])             # 3-ий символ сначала
print(world[-2])            # предпоследний символ
print(world[:5:1])          # первые 5 символов
print(world[:-2:1])         # все кроме 2-ух последних
print(world[::2])           # все с четными индексами
print(world[1::2])          # все с нечетными индексами
print(world[::-1])          # реверс
print(world[::-2])          # через один в обратном порядке
print(len(world))           # длина слова
