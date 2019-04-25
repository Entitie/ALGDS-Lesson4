# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.
# number = input('Введите число: ')

# print(number[::-1])

# Давайте проверим, что лучше число и срез?

import timeit

def srez():
    K = '123456789'
    # return K[::-1]


# print(srez())

def revert():
    K = '123456789'
    K = int(K)
    result = 0
    while K > 0:
        result = result * 10 + K % 10
        K = K // 10
    # return result


# print(revert())

print(timeit.timeit('srez()', setup='from __main__ import srez', number=100000))
print(timeit.timeit('revert()', setup='from __main__ import revert', number=100000))
