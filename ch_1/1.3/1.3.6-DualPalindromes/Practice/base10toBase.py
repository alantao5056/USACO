import math

def base10toBase(num: int, base: int) -> int:
  string = ''
  while num >= base:
    remainder = num % base
    string = str(remainder) + string
    num = math.floor(num / base)
  result = str(num) + string
  return result

print(base10toBase(55, 6))