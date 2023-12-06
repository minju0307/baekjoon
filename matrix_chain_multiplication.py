import sys


def computation(m1, m2):
  ## computation이 가능한지 확인해야 함
  ## 안 되면 error 출력

  if m1[1] != m2[0]:
    return (None, None)

  shape = (m1[0], m2[1])
  computation_count = m1[1] * m2[1] * m1[0]
  ## computation 가능하면 행렬 연산 횟수와 행렬 shape 반환
  return computation_count, shape


def check(matrices, line):
  # print(line)
  stack = []
  count = 0

  ## 행렬 하나만 주어진 경우에는 연산 횟수가 0
  if len(line) == 1:
    return count

  for c in line:
    ## 수식을 읽어가면서 스택에 넣기
    if c == "(" or c == ")":
      stack.append(c)
    else:
      stack.append(matrices[c])

    # print("stack:", stack)

    ## ) 를 만났을 때는 pop
    if c == ")":
      metrix = []
      current = c

      ## (을 만나기 전까지는 꼭 두 개의 행렬이 들어간다.
      while current != "(":
        # print("current:", current)
        # print("metrix:", metrix)
        # print(stack)
        current = stack.pop()
        if type(current) == tuple:
          metrix.append(current)

      local_count, shape = computation(metrix[1], metrix[0])
      if not local_count:
        return "error"
      else:
        count += local_count
        stack.append(shape)

  return count


input = sys.stdin.readline
N = int(input().strip())
matrices = {}

for _i in range(N):
  name, m, n = (input().strip().split())
  matrices[name] = (int(m), int(n))

lines = []
while True:
  line = input().strip()
  if line:
    lines.append(line)
  else:
    break

for line in lines:
  print(check(matrices, line))
