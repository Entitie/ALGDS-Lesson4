# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

number = input('Введите натрульаное число: ')
even_digits = []
deven_digits = []
for el in number:
    if int(el) % 2:
        deven_digits.append(el)
    else:
        even_digits.append(el)

print(f'У числа {number} количество чётных чисел равно {len(even_digits)}, и это {even_digits}')
print(f'А количество НЕчётных чисел равно {len(deven_digits)}, и это {deven_digits}')
