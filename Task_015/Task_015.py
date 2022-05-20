from itertools import accumulate
import operator

n = int(input('Введите число: '))

def get_prods(N):
    return list(accumulate([x for x in range(1, n + 1)], operator.mul))

print(get_prods(n))