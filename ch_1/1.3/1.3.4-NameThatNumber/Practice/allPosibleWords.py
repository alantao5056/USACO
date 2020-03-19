def findAllPosibleWords(num: str) -> list:
  phonePad = {
  '2': ['A','B','C'],
  '3': ['D','E','F'],
  '4': ['G','H','I'],
  '5': ['J','K','L'],
  '6': ['M','N','O'],
  '7': ['P','R','S'],
  '8': ['T','U','V'],
  '9': ['W','X','Y']
  }

  array = []
  word = ''
  allPosibleWords = []
  for i in range(0, len(num)):
    array.append(0)

  current = -1
  while array[0] != 3:
    # adding words
    for k in range(0, len(num)):
      word += phonePad[num[k]][array[k]]
    allPosibleWords.append(word)
    array[-1] += 1
    while array[current] == 3 and current - 1 != len(num) * -1 - 1:
      array[current] = 0
      array[current - 1] += 1
      current -= 1
    current = -1
    word = ''
  return allPosibleWords


print(findAllPosibleWords('4734'))