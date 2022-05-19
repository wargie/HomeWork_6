import random
n = int(input('Введите число: '))

def get_degree(n):
    return [((-3)**i) for i in range(n)]

print (get_degree(n))