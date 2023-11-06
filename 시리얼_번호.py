import sys
import re

N = int(sys.stdin.readline())  # N<=50, O(n^3)까지 가능 
array = []

for i in range(N):
  array.append(sys.stdin.readline().strip())

## 조건 3 : 서로 길이도 같고, 모든 자리수의 합이 같을 때 사전순으로 비교한다. 숫자가 알파벳보다 사전순으로 작다.
array = sorted(array)

## 조건 1 : 길이가 짧은 거 순서로 정렬
array = sorted(array, key=lambda x: len(x))

## 조건 2 : 길이가 같은 경우 자리 수의 합을 비교해서 작은 합을 가지는 것이 먼저 오도록
## 버블 정렬 
for i in range(N-1):
  for j in range(N-i-1):
    if len(array[j]) == len(array[j+1]):
      hap_j = sum([int(j) for j in array[j] if re.search('[0-9]', j)])
      hap_jj = sum([int(j) for j in array[j+1] if re.search('[0-9]', j)])
      if hap_j > hap_jj:
        array[j], array[j+1] = array[j+1], array[j]
      
for i in array:
  print(i)