N = int(input("Введите размер списка: "))
list = list(range(-N, N+1))
print(list)
from functools import reduce
print(reduce(lambda a, b : a * b, list))
