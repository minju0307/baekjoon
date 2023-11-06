import sys
import re

N = int(sys.stdin.readline())  # N<=50
array = []

for i in range(N):
  array.append(sys.stdin.readline().strip())
  
## 조건 1 : 길이가 짧은 거 순서로 정렬
array = sorted(array, key=lambda x: len(x))

## 조건 2 : 길이가 같은 경우 자리 수의 합을 비교해서 작은 합을 가지는 것이 먼저 오도록
## 조건 3 : 사전순으로 비교한다. 숫자가 알파벳보다 사전순으로 작다.
## 버블 정렬 
for i in range(N-1):
  for j in range(N-i-1):
    if len(array[j]) == len(array[j+1]):
      _j = [int(j) for j in array[j] if re.search('[0-9]', j)]
      _jj = [int(j) for j in array[j+1] if re.search('[0-9]', j)]
      if _j and __jj : ## 숫자가 포함되어 있으면
        if sum(_j) > sum(_jj):
          array[j], array[j+1] = array[j+1], array[j]
        elif sum(_j) == sum(_jj):
          if array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]
      else: ## 숫자가 포함되어 있지 않으면 
        if array[j] > array[j+1]:
          array[j], array[j+1] = array[j+1], array[j]
        




