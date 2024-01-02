def solution(numbers):
  numbers = list(map(str, numbers))

  def function(x):
    if len(x) == 4:
      return (x[0], x[1], x[2], x[3])
    elif len(x) == 3:
      return (x[0], x[1], x[2], x[2])
    elif len(x) == 2:
      return (x[0], x[1], x[1], x[1])
    elif len(x) == 1:
      return (x[0], x[0], x[0], x[0])

  numbers = sorted(numbers, key=function, reverse=True)
  # print(numbers)

  answer = ''.join(numbers)
  return str(int(answer))


if __name__ == '__main__':
  numbers = [3, 30, 34, 5, 9]
  print(solution(numbers))
