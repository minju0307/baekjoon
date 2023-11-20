import sys

n = int(sys.stdin.readline().strip())
triangles = []
triangles.append([0])
for i in range(n):
  triangles.append(list(map(int,sys.stdin.readline().strip().split())))

# print(triangles)
dp = [0]*500

for i in range(n, 0, -1):
  triangles[i].insert(0,0)
  for j in range(n-i):
    triangles[i].append(0)

print(triangles)