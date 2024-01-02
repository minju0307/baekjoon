
def solution(numbers):

  ## 조건 1: 큰 순서대로 정렬하기 (문자열은 자동적으로 길이가 길면 더 큰수로 파악한다)
  numbers = list(map(str, numbers))
  numbers = sorted(numbers, reverse=True)

  ## 조건 2: 3이 30보다 앞에 오게 할 수는 없을까? 
  ## 즉, 둘째이하의 숫자가 첫째자리 숫자보다 작다면 길이가 짧은 것이 앞에 오도록 하는 것이다.
  numbers = sorted(numbers, key=lambda x : x[-1], reverse=True)

  answer = ''.join(numbers)
  return answer

if __name__ == '__main__':
  numbers = [3, 30, 34, 5, 9]
  print(solution(numbers))