def solution(answers):
  ## 수포자 패턴 확인
  person1 = [1, 2, 3, 4, 5] * 200
  person2 = [2, 1, 2, 3, 2, 4, 2, 5] * 100
  person3 = [
      3,
      3,
      1,
      1,
      2,
      2,
      4,
      4,
      5,
      5,
  ] * 100

  ## 정답 개수 체크
  correct = [0, 0, 0]

  for idx, number in enumerate(answers):
    if person1[idx] == number:
      correct[0] += 1
    if person2[idx] == number:
      correct[1] += 1
    if person3[idx] == number:
      correct[2] += 1

  ## 최댓값의 인덱스 찾기
  indices = [
      index for index, item in enumerate(correct) if item == max(correct)
  ]
  answer = [i + 1 for i in indices]
  return answer


if __name__ == "__main__":
  answers = [1, 2, 3, 4, 5]
  print(solution(answers))
