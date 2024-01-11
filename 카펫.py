def solution(brown, yellow):

  yellow_half_length = (brown - 4) // 2 

  for i in range(1, (yellow_half_length //2)+1):
      yellow_w, yellow_h = yellow_half_length-i, i
      if yellow_w * yellow_h == yellow:
          break

  answer = [yellow_w+2, yellow_h+2]
  return answer

if __name__=='__main__':
  brown = 24
  yellow = 24
  print(solution(brown, yellow))