dictionary = open('dict.txt', 'r')

def readDict_2(length: int) -> None:
  hash = {}
  word = dictionary.readline().strip()
  while word != '':
    currentHash = hash
    if len(word) == length:
      for char in word:
        if char not in currentHash:
          currentHash[char] = {}
        currentHash = currentHash[char]
    word = dictionary.readline().strip()

  print(hash)

readDict_2(4)