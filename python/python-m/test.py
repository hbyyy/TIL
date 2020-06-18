import random


l1 = [random.randint(1, 5000000) for _ in range(5000000)]
print('sort start')
l1.sort()
print('sort end')
