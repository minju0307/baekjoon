n, _k = map(int, input().split())
num = list(input())
k = _k
stack = []

for i in range(n):
  while (k > 0 and stack and stack[-1] < num[i]):
    ## 만약 스택의 숫자가 지금 숫자보다 작다면
    ## 스택 안에 있는 숫자들을 모두 지워주고
    ## k를 그만큼 감소시킨다. 
    stack.pop()
    k -= 1
  stack.append(num[i])

print(''.join(stack[:n - _k]))

