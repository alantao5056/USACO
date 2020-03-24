"""
ID: alantao2
LANG: PYTHON3
PROG: milk
"""

milkInput = open('milk.in', 'r')
milkOutput = open('milk.out', 'w')

class Farmer:
  def __init__(self, price, amount):
    self.price = price
    self.amount = amount

farmers = []
line = milkInput.readline().strip().split()
amountMilk = int(line[0])
farmersNum = int(line[1])
for i in range(0, farmersNum):
  farmer = milkInput.readline().strip().split()
  farmers.append(Farmer(int(farmer[0]), int(farmer[1])))

farmers = sorted(farmers, key=lambda f: f.price)

money = 0
for f in farmers:
  if f.amount <= amountMilk:
    money += f.amount * f.price
    amountMilk -= f.amount
  else:
    money += amountMilk * f.price
    break

milkOutput.write(str(money) + '\n')