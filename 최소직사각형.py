def solution(sizes):
  max_w = 0
  max_h = 0
  for w, h in sizes:
    max_w = max(max(w, h), max_w)
    max_h = max(min(w, h), max_h)
  answer = max_w * max_h
  return answer


if __name__ == '__main__':
  sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]
  print(solution(sizes))
