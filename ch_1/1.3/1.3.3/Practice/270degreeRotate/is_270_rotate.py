def is_270_rotate(n: int, original: list, transformed: list) -> bool:
  for i in range(0, n):
    for j in range(0, n):
      if original[i][j] != transformed[n - j - 1][i]:
        return False
  return True