def solution(numbers):

  numbers = list(map(str, numbers))
  numbers = sorted(numbers)
  print(numbers)
  for i in range(4):
    numbers = sorted(numbers, key=lambda x: x[-1], reverse=True)
    print(numbers)

  answer = ''.join(numbers)
  return answer


if __name__ == '__main__':
  numbers = [3, 30, 34, 5, 9]
  print(solution(numbers))
