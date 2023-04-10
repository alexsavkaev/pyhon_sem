# 1. Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те,
# в свою очередь, занялись исследованиями статистики за прошлые годы.
# Их интересует, сколько дней длилась самая длинная оттепель.
# Оттепелью они называют период, в который среднесуточная
# температура ежедневно превышала 0 градусов Цельсия. Напишите
# программу, помогающую синоптикам в работе.

# Пользователь вводит число N – общее количество рассматриваемых дней
# (1 ≤ N ≤ 100). В следующих строках располагается N целых чисел.

# Каждое число – среднесуточная температура в соответствующий день.
# Температуры – целые числа и лежат в диапазоне от –50 до 50

length = int(input("Количество дней: "))
mx = 0
current = 0
for i in range(length):
    temp = int(input("Температура: "))
    if temp > 0:
        current += 1
    if temp < 0 or i == length -1:
        if mx < current:
            mx = current
        current = 0
print(f'Максимальная оттепель: {mx} дней.')
