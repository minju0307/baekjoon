import sys
from collections import deque

input = sys.stdin.readline


def check(s, l):
  first = [len(i) for i in s] + [len(l)]  ## 단어들의 길이를 큐에 넣어준다.
  q = deque([first])
  count = 0
  while q:  ## 큐가 비어 있지 않을 때까지
    idx_list = q.popleft()

    ## 종료조건
    if idx_list[-1] == 0:  ## l의 모든 단어들을 순차적으로 찾은 경우에는 true
      return True
    if count == len(l):  ## l의 개수만큼 돌았는데, l의 단어들이 사라지지 않은 경우에는 false
      return False

    word = l[idx_list[-1] - 1]  ## 현재 확인하고자 하는 단어
    # print(word)
    # print(idx_list)
    current = []
    last = idx_list[-1]
    for s_idx, w_idx in enumerate(idx_list[:-1]):
      ## 만약 현재 단어가 특정 앵무새의 마지막 말 단어와 같다면 인덱스를 하나 앞으로 빼준다.
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
