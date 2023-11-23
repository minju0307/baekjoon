import sys
from collections import deque

input = sys.stdin.readline


def check(s, l):
  first = [len(i) for i in s] + [len(l)]
  q = deque([first])
  count = 0
  while q:  ## len(l) 만큼만 확인하기
    idx_list = q.popleft()

    if idx_list[-1] == 0:
      return True
    if count == len(l):
      return False

    word = l[idx_list[-1] - 1]
    # print(word)
    # print(idx_list)
    current = []
    last = idx_list[-1]
    for s_idx, w_idx in enumerate(idx_list[:-1]):
      if w_idx - 1 < len(s[s_idx]) and word == s[s_idx][w_idx - 1]:
        current.append(w_idx - 1)
        last = idx_list[-1] - 1
      else:
        current.append(w_idx)

    count += 1
    current.append(last)
    # print(current)
    q.append(current)


n = int(input().strip())
s = []
for _ in range(n):
  s.append(input().strip().split())
l = input().strip().split()
if check(s, l):
  print("Possible")
else:
  print("Impossible")
