import sys

S = sys.stdin.readline().strip()

## 아카라카 팰린드롬인지 아닌지 확인하는 함수 
## 재귀적으로 들어가서 prefix와 suffix가 각각 아카라카 팰린드롬인지 확인하기 

def check (S):
  ## S의 길이가 1이면 아카라카 팰린드롬
  if len(S) == 1:
    return True
  
  prefix = S[:len(S) // 2]
  suffix = S[len(S) // 2:] if len(S) % 2 == 0 else S[len(S) // 2 + 1:]
  
  ## 만약에 아카라카 팰린드롬이라면, prefix와 suffix도 팰린드롬인지 확인하기 
  if S == S[::-1] and prefix == prefix[::-1] and suffix == suffix[::-1]:
    return check(prefix) and check(suffix)
  ## 만약에 아카라카 팰린드롬이 아니면, 바로 False를 출력하기 
  else:
    return False


if check(S):
  print('AKARAKA')
else:
  print('IPSELENTI')



