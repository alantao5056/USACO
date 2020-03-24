"""
ID: alantao2
LANG: PYTHON3
PROG: milk
"""

milkInput = open('milk.in', 'r')
milkOutput = open('milk.out', 'w')

line = milkInput.readline().strip().split()
farmersNum = int(line[1])
amountMilk = int(line[0])
money = 0

priceIndexList = [0] * 1001

for i in range(0, farmersNum):
  f = milkInput.readline().strip().split()
  priceIndexList[int(f[0])] += int(f[1])

for i in range(0, len(priceIndexList)):
  if amountMilk - priceIndexList[i] >= 0:
    amountMilk -= priceIndexList[i]
    money += priceIndexList[i] * i
  else:
    money += amountMilk * i
    break
milkOutput.write(str(money) + '\n')