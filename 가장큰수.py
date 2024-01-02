## 조건들을 적어보기
## 하나씩 자릿수를 내려가면서 정렬하기 그러니까, 앞 자리수가 큰 것 순서대로 계속 정렬이 되어 있어야 하고, 그것은 뒷 자리수 비교할 때 영향을 끼치면 안됨!
## 길이가 긴 것들이 뒤로 가야함


def solution(numbers):
  i = 0
  numbers = list(map(str, numbers))

  def function(x):
    if i < len(x):
      return (x[i], len(x))
    else:
      return (x[-1], len(x))

  for k in range(4):
    numbers = sorted(numbers, key=function, reverse=True)
    print(numbers)
    i += 1

  answer = ''.join(numbers)
  return str(int(answer))


if __name__ == '__main__':
  numbers = [3, 30, 34, 5, 9]
  print(solution(numbers))
