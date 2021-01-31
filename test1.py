import random

for _ in range(1, 30, 1):
    n = random.randrange(1, 11, step=2)
    k = random.randrange(1, 11)
    print(f'randrange(): n = {n} , k = {k}')
for _ in range(1, 30, 1):
    n = random.randint(1, 11)
    k = random.randint(1, 11)
    print(f'randint(): n = {n} , k = {k}')
# print(f"{n}*{k}={n * k}")
# print(0xffff)
# print(0xffff >> 10)
# print(0b1010 | 0b0101)
# n = 5
# k = 11
# m = 23
# print(f'n = {n} , k = {k}, m = {m}')
# n, k, m = m, n, k
# print(f'n = {n} , k = {k}, m = {m}')
