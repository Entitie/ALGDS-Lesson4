# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
#
# number = input('Введите натрульаное число: ')
# even_digits = []
# deven_digits = []
# for el in number:
#     if int(el) % 2:
#         deven_digits.append(el)
#     else:
#         even_digits.append(el)
#
# print(f'У числа {number} количество чётных чисел равно {len(even_digits)}, и это {even_digits}')
# print(f'А количество НЕчётных чисел равно {len(deven_digits)}, и это {deven_digits}')

# Давайте проверим как лучше определить чётное число. Деление на 2, деление на 2 последнего числа,
# или просто проверить является ли последнее число 0 или 2 или 4 или 6 или 8?

import timeit

def str_even():
    K = '123456789'
    n = int(K[-1::])
    if n % 2:
        answer = 'Not even'
    else:
        answer = 'Even'
    # return answer


# print(str_even())


def str_if_even():
    K = '123456789'
    if K[-1::] == '0' or K[-1::] == '2' or  K[-1::] == '4' or  K[-1::] == '6' or  K[-1::] == '8':
        answer = 'Even'
    else:
        answer = 'Not even'
    # return answer


# print(str_if_even())

def int_even():
    K = '123456789'
    K = int(K)
    if K % 2:
        answer = 'Not even'
    else:
        answer = 'Even'
    # return answer


# print(int_even())

def int_last_even():
    K = '123456789'
    K = int(K) % 10
    if K % 2:
        answer = 'Not even'
    else:
        answer = 'Even'
    # return answer


# print(int_last_even())

def int_if_last_even():
    K = '123456789'
    K = int(K) % 10
    if K == 0 or K == 2 or K == 4 or K == 6 or K == 8:
        answer = 'Even'
    else:
        answer = 'Not even'
    # return answer


# print(int_if_last_even())

print(timeit.timeit('str_even()', setup='from __main__ import str_even', number=100000))
print(timeit.timeit('str_if_even()', setup='from __main__ import str_if_even', number=100000))
print(timeit.timeit('int_even()', setup='from __main__ import int_even', number=100000))
print(timeit.timeit('int_last_even()', setup='from __main__ import int_last_even', number=100000))
print(timeit.timeit('int_if_last_even()', setup='from __main__ import int_if_last_even', number=100000))
