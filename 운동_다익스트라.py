import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]
distance = [[INF] * (v + 1) for _ in range(v + 1)]
heap = []

# dist, 위치1, 위치2 순서로 heap에 push
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append([c, b])
    distance[a][b] = c
    heapq.heappush(heap, [c, a, b])

while heap:
    dist, first, last = heapq.heappop(heap)
    if first == last:
        print(dist)
        break

    if distance[first][last] < dist:
        continue

    for i, j in graph[last]:
        # first -> last -> j
        n_distance = i + dist
        # (first->last->j vs first -> j) if more cheap, change n_distance
        if distance[first][j] > n_distance:
            distance[first][j] = n_distance
            heapq.heappush(heap, [distance[first][j], first, j])
else:
  print(-1)