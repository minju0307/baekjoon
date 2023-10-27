N = int(input())  ## N의 개수가 벡민이기 떄문에 linear time 으로 짜야함
length = []
for i in range(N):
  length.append(int(input()))

length = sorted(length, reverse=True)

for idx, number in enumerate(length):
  max_len = number

  if len(length[idx:]) == 3:  ## 남은 것이 3개이면은
    if max_len < length[idx + 1] + length[idx + 2]:  ## 삼각형을 만들 수 있는 조건
      print(max_len + length[idx + 1] + length[idx + 2])
      break
    else:
      print(-1)
      break
  else:
    if max_len < length[idx + 1] + length[idx + 2]:  ## 삼각형을 만들 수 있는 조건
      print(max_len + length[idx + 1] + length[idx + 2])
      break
    else:
      continue
