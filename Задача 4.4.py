# Задача № 4: Представлен список чисел. Определите элементы списка, не имеющие повторений.
#             Сформируйте итоговый массив чисел, соответствующих требованию.
#             Элементы выведите в порядке их следования в исходном списке.
#             Для выполнения задания обязательно используйте генератор.
#             Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
#             Результат: [23, 1, 3, 10, 4, 11]
# Решение:

# исходный список
original_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

# (original_list.count(i) < 2) - функция count возвращает количество вхождений подстроки (которая указана в скобках)
# иными словами функция count высчитывает количество текущего элемента в списке, если возвращается значение меньше 2-ух
# то это значение уникально в этом списке и оно добавляется в новый список
finished_list = [i for i in original_list if (original_list.count(i) < 2)]

print(f'Дано:      {original_list}')
print(f'Результат: {finished_list}')
