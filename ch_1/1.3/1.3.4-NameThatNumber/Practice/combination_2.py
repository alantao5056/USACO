def generateBase3Combination(length: int) -> None:
  list = []
  for i in range(0, length):
    list.append(0)

  current = 0
  while list[-1] != 3:
    print(list)
    list[0] += 1
    while list[current] == 3 and current + 1 != length:
      list[current] = 0
      list[current + 1] += 1
      current += 1
    current = 0

generateBase3Combination(5)