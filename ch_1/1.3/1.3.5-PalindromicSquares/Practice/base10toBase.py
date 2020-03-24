import math

def base10toBase(num: int, base: int) -> int:
  numsToLetters = {
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F',
    16: 'G',
    17: 'H',
    18: 'I',
    19: 'J',
    20: 'K'
  }
  string = ''
  while num >= base:
    remainder = num % base
    if remainder > 9:
      string = numsToLetters[remainder] + string
    else:
      string = str(remainder) + string
    num = math.floor(num / base)
  if num > 9:
    string = numsToLetters[num] + string
    result = string
  else:
    result = str(num) + string
  return result

print(base10toBase(14400, 11))
