# Последовательность Фибоначчи


def fib_n(num):             # ищем номер числа в последовательности
    n = 1                   # счетчик
    f0 = 0                  # начальные значения последовательнсти
    f1 = f = 1
    while num != f:
        f = f0 + f1         # вычисляем числа Ф.
        f0 = f1
        f1 = f
        n += 1
        if num == f:        # введенное число является числом Ф.
            return n
        elif n == 50:       # введенное число не попало в первые 50 чисел Ф.
            return '-1'


f_num = int(input())
print(fib_n(f_num))