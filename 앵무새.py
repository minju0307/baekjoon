import sys
from collections import deque

input = sys.stdin.readline


def check(s, l):
  first = [len(i) for i in s]
  q = deque([first])

  for word in l[::-1]:  ## len(l) 만큼만 확인하기
    print(word)
    idx_list = q.popleft()
    print(idx_list)
    current = []
    for s_idx, w_idx in enumerate(idx_list):
      if w_idx - 1 < len(s[s_idx]) and word == s[s_idx][w_idx - 1]:
        current.append(w_idx - 1)
      else:
        current.append(w_idx)

    print(current)
    q.append(current)

  last = q.popleft()
  return all(count == 0 for count in last)


n = int(input().strip())
s = []
for _ in range(n):
  s.append(input().strip().split())
l = input().strip().split()
if check(s, l):
  print("Possible")
else:
  print("Impossible")
