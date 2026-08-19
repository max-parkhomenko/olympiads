# Условие: Светофор цикличен: a секунд зелёный, затем b секунд красный. В момент 0 - зелёный. Определите цвет в момент времени t (секунд от старта).
# Формат входных данных: Три целых числа в отдельных строках: a, b, t.
# Формат выходных данных: Одно слово: GREEN или RED.
# Ограничения: 1 ≤ a, b, t ≤ 10^9.
# Пример
# Ввод:

# 3
# 2
# 4
# Вывод:

# RED

a = int(input())
b = int(input())
t = int(input())

if t == 0:
    result = "GREEN"
else:
    if t % b == 0:
        result = "RED"
    else:
        result = "GREEN"

cycle_time = a + b
t_percent = t % cycle_time
if t_percent < a:
    result = "GREEN"
else:
    result = "RED"

print(result)