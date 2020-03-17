def isReflection(n: int, original: list, transformed: list) -> bool:
  for i in range(0, n):
    for j in range(0, n):
      if original[i][j] != transformed[i][n - j - 1]:
        return False
  return True