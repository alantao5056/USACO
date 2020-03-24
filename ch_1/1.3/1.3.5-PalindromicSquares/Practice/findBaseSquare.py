import math

def base10toBase(num: int, base: int) -> int:
  string = ''
  while num >= base:
    string = str(num % base) + string
    num = math.floor(num / base)
  result = str(num) + string
  return int(result)

def findBaseSquare(base: int) -> list:
  baseSquare = []
  for i in range(1, 301):
    baseSquare.append([base10toBase(i, base), base10toBase(i ** 2, base)])
  return baseSquare

print(findBaseSquare(5))