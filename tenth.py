# Дана последовательность из N целых чисел. Рассмотрим все пары элементов последовательности, которые находятся на одинаковом расстоянии от её концов. Такие пары будем называть симметричными.

# Например, в последовательности [3, 7, 2, 8, 1]:

# 	1-я пара: первый (3) и последний (1) элементы

# 	2-я пара: второй (7) и предпоследний (8) элементы

# 	3-я пара: средний элемент (2) с самим собой (если длина нечётная)

# Задача:

# Для каждой симметричной пары вычислить:

# 	Сумму, если оба числа чётные

# 	Произведение, если оба числа нечётные

# 	0, если числа разной чётности

# Найдите максимальное из полученных значений.

def get_symmetrical_pair_at(iterable: list, index: int):
    return (iterable[index], iterable[-index-1])

def do_action(pair: tuple[int, int]) -> int:
    if pair[0] % 2 == 0:
        if pair[1] % 2 == 0:
            return sum(pair)
        else:
            return 0
    
    if pair[1] % 2 == 0:
        return 0
    else:
        return pair[0] * pair[1]
    
def get_all_pairs(iterable: list) -> list[tuple[int, int]]:
    result = []
    for i in range(len(iterable) // 2):
        result.append(get_symmetrical_pair_at(iterable, i))
    if len(iterable) % 2 != 0:
        pair_spec = get_symmetrical_pair_at(iterable, i + 1)
        result.append(pair_spec)
    return result

    
l = [3, 7, 2, 8, 1]
results = []
pairs = get_all_pairs(l)
for pair in pairs:
    action_result = do_action(pair)
    results.append(action_result)

print(max(results))