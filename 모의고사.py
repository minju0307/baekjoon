## 런타임 에러는 시간 에러가 아님 
## 리스트의 범위를 초과했거나 0으로 나눴거나 등의 문제가 일어났을 때에도 런타임 에러가 일어날 수 있음 

def solution(answers):

## 수포자 패턴 확인
person1 = [1,2,3,4,5]*2000
person2 = [2,1,2,3,2,4,2,5]*1500
person3 = [3,3,1,1,2,2,4,4,5,5]*1000
print(len(person1))
print(len(person2))
print(len(person3))

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
max_correct = max(correct)
answer = [index+1 for index, item in enumerate(correct) if item == max_correct]

return answer


if __name__ == "__main__":
  answers = [1, 2, 3, 4, 5]
  print(solution(answers))
