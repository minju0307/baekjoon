import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input().strip())
dict = defaultdict(int)

for i in list(map(int, input().strip().split())):
  dict[i] += 1

M = int(input().strip())
for i in list(map(int, input().strip().split())):
  print(dict[i], end=' ')
