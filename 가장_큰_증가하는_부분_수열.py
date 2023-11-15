import sys

n = int(sys.stdin.readline().strip())
array = list(map(int, sys.stdin.readline().strip().split()))
array.insert(0, 0)  ## dp 테이블과의 인덱스를 맞추기 위해서 (합이니까 0을 추가하는 것은 괜찮음)

## 그 증가수열의 합을 저장하는 dp 테이블 정의
hap_dp = [0] * 1001
hap_dp[0] = 0

## O(n^2) 알고리즘으로 몇개가 증가하고 있는지 확인하고 그 합을 저장하는 DP 테이블 정의하기
for idx, value in enumerate(array):
  print(value)
  max_hap = 0
  for previous_value in array[:idx]:
    if previous_value < value:
      print(max_hap)
      max_hap = max(max_hap, previous_value)
  hap_dp[idx] = max_hap + value
  print()

print(array)
print(hap_dp[:len(array)])
print(max(hap_dp))
