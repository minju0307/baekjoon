N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())), reverse=True)

S = 0
for idx in range(N):
  S += A[idx] * B[idx]

print(S)
