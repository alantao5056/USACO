def isCombination(n: int, original: list, transformed: list) -> bool:
  rotate_90 = True
  rotate_180 = True
  rotate_270 = True
  for i in range(0, n):
    for j in range(0, n):
      iReflect = i
      jReflect = n - j - 1
      if original[i][j] != transformed[jReflect][n - iReflect - 1] and rotate_90 == True:
        rotate_90 = False
      if original[i][j] != transformed[n - iReflect - 1][n - jReflect - 1] and rotate_180 == True:
        rotate_180 = False
      if original[i][j] != transformed[n - jReflect - 1][iReflect] and rotate_270 == True:
        rotate_270 = False
      if rotate_90 == False and rotate_180 == False and rotate_270 == False:
        return False
  if rotate_90 == True or rotate_180 == True or rotate_270 == True:
    return True