def baseConvert(num: int, base: int) -> int:
  numStr = str(num)
  base10Num = 0
  value = 0
  for i in range(len(numStr) - 1, -1, -1):
    base10Num += base ** value * int(numStr[i])
    value += 1
  return base10Num

print(baseConvert(233, 5))