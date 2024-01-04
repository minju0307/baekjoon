from collections import deque


def solution(arr):
  answer = []
  dq = deque()
  dq.append(arr[0])

  for i in range(1, len(arr)):
    current = dq[-1]
    if current != arr[i]:
      dq.append(arr[i])

  return answer


if __name__ == "__main__":
  print(solution([1, 1, 3, 3, 0, 1, 1]))
