import sys

n = int(sys.stdin.readline().strip())
triangles = []
triangles.append([0])
for i in range(n):
  triangles.append(list(map(int, sys.stdin.readline().strip().split())))

## dp 테이블 = 삼각형 모양으로 현재까지의 최댓값이 무엇인지 담을 수 있도록 만들기
dp = [[0] * i for i in range(len(triangles))]
dp[0] = [0]

# print(triangles)
# print(dp)

for i in range(1, n + 1):
  # print(f"***{i}***")
  ## dp 테이블에 저장하기
  for idx, value in enumerate(triangles[i]):
    if idx == 0:
      dp[i][idx] = dp[i - 1][idx] + value
    elif idx == len(triangles[i]) - 1:
      dp[i][idx] = dp[i - 1][idx - 1] + value
    else:
      dp[i][idx] = max(dp[i - 1][idx - 1] + value, dp[i - 1][idx] + value)

  # print(dp)

print(max(dp[-1]))
