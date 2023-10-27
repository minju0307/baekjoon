N = int(input())  ## N의 개수가 벡민이기 떄문에 linear time 으로 짜야함
length = []
for i in range(N):
  length.append(int(input()))
length = sorted(length, reverse=True)
answer = -1

for i in range(N-1):
  if length[i] < length[i+1] + length[i+2]:
    answer = length[i] + length[i+1] + length[i+2]
    break

print(answer)
