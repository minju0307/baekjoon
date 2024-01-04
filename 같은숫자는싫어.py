def solution(arr):
  answer = []
  answer.append(arr[0])

  for i in range(1, len(arr)):
    current = answer[-1] 
    if current != arr[i]:
        answer.append(arr[i])

  return answer


if __name__ == "__main__":
  print(solution([1, 1, 3, 3, 0, 1, 1]))
