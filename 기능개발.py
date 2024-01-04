from collections import deque


def solution(progresses, speeds):
  answer = []
  dq = deque(progresses)
  print(dq)
  while dq:
    print("***")
    ## 하루치 개발 진도량을 반영하기
    for idx, work in enumerate(progresses):
      dq[idx] = dq[idx]+ speeds[idx]
    print(dq)

    ## popleft 하면서 100이 넘는 게 있다면 빼버리기
    deploy = 0  ## 오늘 배포 가능한 것의 숫자
    current = dq.popleft()
    while current >= 100:
      deploy += 1
      current = dq.popleft()
    if current < 100:
      dq.appendleft(current)
    print(dq)

    if deploy > 0:
      answer.append(deploy)
    print(deploy)

  return answer


if __name__ == "__main__":
  print(solution([93, 30, 55], [1, 30, 5]))
