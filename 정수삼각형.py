import sys

n = int(sys.stdin.readline().strip())
triangles = []
triangles.append([0])
for i in range(n):
  triangles.append(list(map(int,sys.stdin.readline().strip().split())))

# print(triangles)
dp = [0] * 501
dp[1] = triangles[1][0]

for i in range(2, n + 1):

  ## 계산하기 편하도록 리스트를 조정하기
  triangles[i].insert(0, 0)
  for j in range(n - i):
    triangles[i].append(0)

  ## 현재 level에서 모든 경우의 수를 합한 것을 저장하여 최상의 조합이 무엇인지 찾기

print(triangles)
print(dp[:n])
