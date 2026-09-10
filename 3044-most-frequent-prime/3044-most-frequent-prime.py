from collections import Counter
from typing import List
class Solution:
  def mostFrequentPrime(self, mat: List[List[int]]) -> int:
    m, n = len(mat), len(mat[0])
    freq = Counter()

    def is_prime(val: int) -> bool:
      if val <= 1:
        return False
      for i in range(2, int(val**0.5) + 1):
        if val % i == 0:
          return False
      return True
    directions = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]

    for r in range(m):
      for c in range(n):
        for dr, dc in directions:
          curr_num = mat[r][c]
          nr, nc = r + dr, c + dc
          while 0 <= nr < m and 0 <= nc < n:
            curr_num = curr_num * 10 + mat[nr][nc]
            if curr_num > 10 and is_prime(curr_num):
              freq[curr_num] += 1
            nr += dr
            nc += dc
    if not freq:
      return -1
    max_freq = max(freq.values())
    return max(val for val, count in freq.items() if count == max_freq)