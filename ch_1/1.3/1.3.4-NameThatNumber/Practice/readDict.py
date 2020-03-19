dictionary = open('dict.txt', 'r')

def readDict(length: int) -> set:
  hash = set()
  while dictionary.readline().strip() != 'ZACCHEUS':
    word = dictionary.readline().strip()
    if len(word) == length:
      hash.add(word)
  return hash

print(readDict(8))