from itertools import permutations


def is_prime(num):
  if num == 1 or num == 0:
    return False
  for i in range(2, num):
    if num % i == 0:
      return False
  return True


def solution(numbers):
  answer = 0
  prime = []
  paper = [i for i in numbers]
  for k in range(1, len(paper) + 1):
    permut = list(permutations(paper, k))
    permut_nums = list(set([int(''.join(i)) for i in permut]))
    for num in permut_nums:
      if is_prime(num):
        if num not in prime:
          answer += 1
          prime.append(num)
  return answer


if __name__ == "__main__":
  numbers = "011"
  print(solution(numbers))
