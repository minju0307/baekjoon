import sys

input = sys.stdin.readline
INF = sys.maxsize

v, e = map(int, input().split())

## 그래프 초기화
graph = [[INF] * (v + 1) for _ in range(v + 1)]

for i in range(1, v + 1):
  for j in range(1, v + 1):
    if i == j:
      graph[i][j] = 0

## 초기 간선 정보 입력 받기
for _ in range(e):
  a, b, c = map(int, input().split())
  graph[a][b] = c

## 플루이드 워셜 알고리즘 수행 & 사이클 찾기
min_cycle = INF
for k in range(1, v + 1):
  for a in range(1, v + 1):
    for b in range(1, v + 1):
      if a == b:
        continue
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
      min_cycle = min(min_cycle, graph[a][b] + graph[b][a])

# for line in graph:
#   print(line)

## 답변 출력하기
if min_cycle == INF:
  print(-1)
else:
  print(min_cycle)
