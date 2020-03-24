"""
ID: alantao2
LANG: PYTHON3
PROG: milk
"""

import math

class Farmer:
  def __init__(self, price, amount):
    self.price = price
    self.amount = amount

milkInput = open('milk.in', 'r')
milkOutput = open('milk.out', 'w')

farmers = []
line = milkInput.readline().strip().split()
amountMilk = int(line[0])
farmersNum = int(line[1])
for i in range(0, farmersNum):
  farmer = milkInput.readline().strip().split()
  farmers.append(Farmer(int(farmer[0]), int(farmer[1])))

if amountMilk == 0:
  milkOutput.write('0\n')
  exit()

cheapestPrize = math.inf
cheapestPrizeIndex = 0
money = 0
while amountMilk > 0:
  for i in range(0, len(farmers)):
    if farmers[i].price < cheapestPrize:
      cheapestPrizeIndex = i
      cheapestPrize = farmers[cheapestPrizeIndex].price
  cheapestAmount = farmers[cheapestPrizeIndex].amount
  if amountMilk > cheapestAmount:
    money += cheapestPrize * cheapestAmount
    amountMilk -= cheapestAmount
    farmers.pop(cheapestPrizeIndex)
  else:    
    break
  cheapestPrize = math.inf
milkOutput.write(str(money + amountMilk * cheapestPrize) + '\n')