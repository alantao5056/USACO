def generateBase3Combination(length: int) -> None:
  list = []
  for i in range(0, length):
    list.append(0)
  
  current = -1
  while list[0] != 3:
    print(list)
    list[-1] += 1
    while list[current] == 3 and current - 1 != length * -1 - 1:
      list[current] = 0
      list[current - 1] += 1
      current -= 1
    current = -1

  # done = False
  # endIndex = length * -1 - 1
  # while done == False:
  #   print(list)
  #   current = -1
  #   while True:
  #     list[current] += 1
  #     if list[current] == 3:
  #       list[current] = 0
  #       current -= 1
  #       if current == endIndex:
  #         done = True
  #         break
  #     else:
  #       break

generateBase3Combination(5)