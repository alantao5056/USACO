import math

def toString(num: int, target: int) -> int:
  if target <= len(str(num)):
    return num
  else:
    num = str(num)
    num = list(num)
    length = len(num)
    while length < target - 1:
      length = len(num)
      num.insert(0, 0)
    strings = [str(integer) for integer in num]
    a_string = "".join(strings)
    return a_string

print(toString(5, 5))

def getAllPalindromes(start: int, end: int) -> list:
  if start <= 2:
    palindromes = [2]
  else:
    palindromes = []
  for i in range(1, len(str(end)) + 1):
    if i == 1:
      for j in range(3, 10):
        if j % 2 != 0 and j <= end and j >= start:
          palindromes.append(j)
    else:
      integers = [1]
      halfLen = math.floor(i / 2)
      for j in range(0, halfLen - 1):
        integers.append(0)
      strings = [str(integer) for integer in integers]
      a_string = "".join(strings)
      integers = int(a_string)

      if i % 2 != 0:
        for k in range(0, integers * 10, 2):
          k = toString(k, halfLen)
          for num in range(0, 10):
            pal = f'{str(k)[::-1]}{num}{k}'
            if pal[0] != '0':
              pal = int(pal)
              if pal <= end and pal >= start:
                palindromes.append(pal)
      else:
        for k in range(0, integers * 10, 2):
          k = toString(k, halfLen)
          pal = f'{str(k)[::-1]}{k}'
          if pal[0] != '0':
            pal = int(pal)
            if pal <= end and pal >= start:
              palindromes.append(pal)
  return palindromes