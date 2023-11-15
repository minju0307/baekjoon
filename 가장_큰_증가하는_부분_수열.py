import sys

n = int(sys.stdin.readline().strip())
array = list(map(int, sys.stdin.readline().strip().split()))
array.insert(0, 0)  ## dp 테이블과의 인덱스를 맞추기 위해서 (합이니까 0을 추가하는 것은 괜찮음)

## array의 현재 값보다 작은 값이 몇 개 있는지 찾는 dp 테이블 정의
dp = [0] * 1001
dp[0] = 0

## 그 증가수열의 합을 저장하는 dp 테이블 정의
hap_dp = [0] * 1001
hap_dp[0] = 0

## O(n^2) 알고리즘으로 몇개가 증가하고 있는지 확인하고 그 합을 저장하는 DP 테이블 정의하기
for idx, value in enumerate(array):
  count = 0
  hap = 0
  for previous_value in array[:idx]:
    if value > previous_value:
      count += 1
      hap += previous_value
  dp[idx] = count
  hap_dp[idx] = hap + value

print(array)
print(dp[:len(array)])
print(hap_dp[:len(array)])
print(max(hap_dp))
