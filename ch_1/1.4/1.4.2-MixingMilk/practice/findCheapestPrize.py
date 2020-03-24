import math

def findCheapestPrize(list: list) -> int:
  cheapestPrize = math.inf
  for i in range(0, len(list)):
    prize = int(list[i][0])
    if prize < cheapestPrize:
      cheapestPrize = prize
  return cheapestPrize

print(findCheapestPrize([['5', '20'], ['9', '40'], ['3', '10'], ['8', '80'], ['6', '30']]))