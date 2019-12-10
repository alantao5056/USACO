"""
ID: alantao2
LANG: PYTHON3
PROG: gift1
"""

import math

inputGift1 = open('gift1.in', 'r')
outputGift1 = open('gift1.out', 'w')

peopleNum = int(inputGift1.readline())

people = []
peopleWallet = {}

for num in range(peopleNum):
  key = inputGift1.readline().strip()
  people.append(key)
  peopleWallet[key] = 0

name = inputGift1.readline().strip()

while(name != ''):
  money, friendsNum = map(int, inputGift1.readline().split())
  if(friendsNum != 0):
    peopleWallet[name] -= money
    peopleWallet[name] += money % friendsNum
    print(f'{name} has ${money} and {friendsNum} friends.')
    moneyToGet = int(math.floor(money / friendsNum))
    for i in range(friendsNum):
      peopleWallet[inputGift1.readline().strip()] += moneyToGet
  name = inputGift1.readline().strip()
print(peopleWallet)
for p in people:
  outputGift1.write(f"{p} {peopleWallet[p]}\n")
outputGift1.close()