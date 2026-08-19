# Условие: В столовой выдача одной порции занимает 1 минуту. После каждых a выданных порций повар делает перерыв на b минут, но после выдачи последней порции перерыв не нужен. Нужно выдать n порций. Сколько минут это займёт?
# Формат входных данных: Три целых числа в отдельных строках: a, b, n.
# Формат выходных данных: Одно целое число - общее время выдачи.
# Ограничения: 1 ≤ a, b, n ≤ 10^9.
# Пример
# Ввод:

# 4
# 5
# 10
# Вывод:

# 20

a = int(input())
b = int(input())
n = int(input())

# result = 0
# portions_given_after_break = 0
# portions_given = 0

# for i in range(n):
#     portions_given_after_break += 1
#     portions_given += 1
#     result += 1
#     if portions_given_after_break < a:
#         continue
#     else:
#         if portions_given == n:
#             break
#         portions_given_after_break = 0
#         result += b

breaks_count = (n - 1) // a
result = breaks_count * b + n

print(result)