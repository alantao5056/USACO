"""
ID: alantao2
LANG: PYTHON3
PROG: namenum
"""

nameNumInput = open('namenum.in', 'r')
num = nameNumInput.readline().strip()
nameNumOutput = open('namenum.out', 'w')
dictionary = open('dict.txt', 'r')

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

# code...

hash = set()
word = dictionary.readline().strip()
length = len(num)
while word != 'ZACCHEUS':
  if len(word) == length:
    hash.add(word)
  word = dictionary.readline().strip()

array = []
word = ''
for i in range(0, length):
  array.append(0)

current = -1
result = False
while array[0] != 3:
  # adding words
  for k in range(0, length):
    word += phonePad[num[k]][array[k]]
  if word in hash:
    nameNumOutput.write(word + '\n')
    result = True
  array[-1] += 1
  while array[current] == 3 and current - 1 != length * -1 - 1:
    array[current] = 0
    array[current - 1] += 1
    current -= 1
  current = -1
  word = ''

if result == False:
  nameNumOutput.write('NONE\n')
