def solution(numbers):
  i = 0
  numbers = list(map(str, numbers))

  # numbers = sorted(numbers, reverse=True)
  # print(numbers)

  def function(x):
    if i < len(x):
      return x[i]
    else:
      return x[-1]

  for i in range(4):
    numbers = sorted(numbers, key=function, reverse=True)
    print(numbers)
    i += 1

  answer = ''.join(numbers)
  return str(int(answer))


if __name__ == '__main__':
  numbers = [3, 30, 34, 5, 9]
  print(solution(numbers))
