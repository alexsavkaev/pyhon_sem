# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону (т.е. 
# не меньше заданного минимума и не больше заданного максимума)

# Input:
# 1, 3, 7, 10, 5, 8
# 4
# 8
# Output:
# 2(7), 4(5), 5(8)
def find_indexes(lst, min_val, max_val):
    indexes = []
    for i, x in enumerate(lst):
        if min_val <= x <= max_val:
            indexes.append(i)
    return indexes

lst = list(map(int, input("Введите элементы списка через пробел: ").split()))
min_val = int(input("Введите минимальное значение: "))
max_val = int(input("Введите максимальное значение: "))
print(find_indexes(lst, min_val, max_val))