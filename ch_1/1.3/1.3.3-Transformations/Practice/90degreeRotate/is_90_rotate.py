def is90Rotate(n: int, original: list, transformed: list) -> bool:
  for i in range(0, n):
    for j in range(0, n):
      if original[i][j] != transformed[j][n - i - 1]:
        return False
  return True