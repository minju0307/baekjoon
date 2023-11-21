import sys
from collections import deque

input = sys.stdin.readline


def bfs(words):
  w1, w2, w3 = words
  dp = [[0] * (len(w2) + 1) for _ in range(len(w1) + 1)]
  dq = deque([(len(w1), len(w2), len(w3))])

  while dq:
    w1_idx, w2_idx, w3_idx = dq.popleft()

    if w1_idx == w2_idx == w3_idx == 0:
      return True
    elif w3_idx == 0:
      return False

    if w1_idx > 0 and w1[w1_idx - 1] == w3[w3_idx - 1] and dp[w1_idx - 1][w2_idx] == 0:
      dp[w1_idx - 1][w2_idx] = 1
      dq.append((w1_idx - 1, w2_idx, w3_idx - 1))

    if w2_idx > 0 and w2[w2_idx - 1] == w3[w3_idx - 1] and dp[w1_idx][w2_idx - 1] == 0:
      dp[w1_idx][w2_idx - 1] = 1
      dq.append((w1_idx, w2_idx - 1, w3_idx - 1))

  else:
    return False


n = int(input().strip())
for i in range(n):
  words = (input().strip().split())

  if bfs(words):
    print(f"Data set {i+1}: yes")
  else:
    print(f"Data set {i+1}: no")
