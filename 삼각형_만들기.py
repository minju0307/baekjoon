import sys

N = int(sys.stdin.readline())  ## N의 개수가 벡민이기 떄문에 linear time 으로 짜야함
length = sorted([int(sys.stdin.readline()) for _ in range(N)], reverse=True)
answer = -1

for i in range(N-2):
  if length[i] < length[i+1] + length[i+2]:
    answer = length[i] + length[i+1] + length[i+2]
    break

print(answer)
