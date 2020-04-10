from random import randrange
from timeit import default_timer as timer

N = 1000000
original = [] * N
for i in range(N):
  original.append(randrange(N))

list = [False] * N
set = set()
for num in original:
  list[num] = True
  set.add(num)

frozenset = frozenset(set)

start = timer()
for i in range(100):
  for j in range(N):
    found = list[j]
end = timer()
print(f'list: {end - start}')

start = timer()
for i in range(100):
  for j in range(N):
    found = j in set
end = timer()
print(f'set: {end - start}')

start = timer()
for i in range(100):
  for j in range(N):
    found = j in frozenset
end = timer()
print(f'frozenset: {end - start}')

