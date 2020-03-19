"""
ID: alantao2
LANG: PYTHON3
PROG: transform
"""

transformationsInput = open('transform.in','r')
transformationsOutput = open('transform.out', 'w')

original = []
transformed = []

n = int(transformationsInput.readline().strip())
for i in range(0, n):
  original.append(transformationsInput.readline().strip())

for i in range(0, n):
  transformed.append(transformationsInput.readline().strip())

# code...

rotate_90 = True
rotate_180 = True
rotate_270 = True
reflection = True
reflection_90 = True
reflection_180 = True
reflection_270 = True
noChange = True

for i in range(0, n):
  for j in range(0, n):
    # 90 degree rotation check
    if rotate_90 and original[i][j] != transformed[j][n - i - 1]:
      rotate_90 = False
    # 180 degree rotation check
    if rotate_180 and original[i][j] != transformed[n - i - 1][n - j - 1]:
      rotate_180 = False
    # 270 degree rotation check
    if rotate_270 and original[i][j] != transformed[n - j - 1][i]:
      rotate_270 = False
    # reflection check
    if reflection and original[i][j] != transformed[i][n - j - 1]:
      reflection = False
    # no change check
    if noChange and original[i][j] != transformed[i][j]:
      noChange = False
    # reflection rotation 90 check
    jReflect = n - j - 1
    if reflection_90 and original[i][j] != transformed[jReflect][n - i - 1]:
      reflection_90 = False
    # reflection rotation 180 check
    if reflection_180 and original[i][j] != transformed[n - i - 1][n - jReflect - 1]:
      reflection_180 = False
    # reflection rotation 270 check
    if reflection_270 and original[i][j] != transformed[n - jReflect - 1][i]:
      reflection_270 = False

# checking results
result = '7'
if rotate_90:
  result = '1'
elif rotate_180:
  result = '2'
elif rotate_270:
  result = '3'
elif reflection:
  result = '4'
elif reflection_90 or reflection_180 or reflection_270:
  result = '5'
elif noChange:
  result = '6'

# inputing results
transformationsOutput.write(result + '\n')