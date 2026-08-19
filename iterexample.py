from itertools import combinations

prices = [10, 20, 30, 40]

for trio in combinations(prices, 3):
    print(trio)