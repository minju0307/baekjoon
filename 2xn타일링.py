import sys

n = int(sys.stdin.readline().strip())

array = [0]*1001 
array[1] = 1
array[2] = 2

for i in range(3, n+1):
  array[i] = array[i-1] + array[i-2]

print(array[n]%10007)
  