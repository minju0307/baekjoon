import sys

input = sys.stdin.readline

n, k = map(int, input().strip().split())
numbers = list(map(int, list(input().strip())))

final_number = [0] * (n - k)
next_start = 0

for idx in range(n - k):
  ## 현재 칸에 들어갈 수 있는 숫자들
  # print("***")
  current = numbers[next_start:(k + idx + 1)]
  # print(current)

  ## 그 중 가장 큰 숫자를 넣어주기
  final_number[idx] = max(current)
  # print(final_number)

  ## 넣어준 숫자 이후로 current를 설정하기
  next_start = current.index(final_number[idx]) + next_start + 1
  # print(next_start)

print(''.join([str(i) for i in final_number]))
