import sys
import heapq

input = sys.stdin.readline
INF = 10001

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
    dist, start, end = heapq.heappop(heap)
    if start == end:
        print(dist)
        break

    if distance[start][end] < dist:
        continue

    for cost, new_end in graph[end]:
        n_distance = cost + dist
        if distance[start][new_end] > n_distance:
            distance[start][new_end] = n_distance
            heapq.heappush(heap, [distance[start][new_end], start, new_end])
else:
  print(-1)