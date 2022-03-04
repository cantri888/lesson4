# Задача № 3: Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Решите задание в одну строку.
#             Подсказка: используйте функцию range() и генератор.
# Решение:

# генератор который формирует список т.к. генератор помещен в [] скобки
# читаем генератор: для текущего числа в диапазоне от 20 до 241 (не включительно) добавляем в список,
#                        если текущее число не будет иметь остатка от деления на 20 или 21
print(f'От 20 до 240 найдены числа, кратные 20 или 21: {[i for i in range(20, 241) if (i % 20 == 0) or (i % 21 == 0)]}')
