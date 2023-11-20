import sys

n = int(sys.stdin.readline().rstrip())
word_list = []
for i in range(n):
  word_list.append(sys.stdin.readline().strip().split())

for idx, (w1, w2, w3) in enumerate(word_list):
  w1_index = 0
  w2_index = 0
  answer = 'yes'
  ## w3에 있는 단어들을 차례대로 살피면서
  ## w1나 w2의 단어들이 순차적으로 올 수 있는지 확인하기
  # print(f"***{w3}***")
  for c in w3:
    # print(c)
    ## 만약 w1와 w2의 현재 index의 단어가 같으면
    if w1_index < len(w1) and w2_index < len(
        w2) and w1[w1_index] == w2[w2_index]:
      ## index가 더 적은 쪽에 넣어준다. 
      if w1_index <= w2_index:
        if w1_index < len(w1) and c == w1[w1_index]:
          w1_index += 1
          continue
        elif w2_index < len(w2) and c == w2[w2_index]:
          w2_index += 1
          continue
        else:
          answer = 'no'
          break
      else:
        if w2_index < len(w2) and c == w2[w2_index]:
          w2_index += 1
          continue
        elif w1_index < len(w1) and c == w1[w1_index]:
          w1_index += 1
          continue
        else:
          answer = 'no'
          break
    ## 단어가 겹치지 않을 때는 순차적으로 w1, w2에 들어있는지 확인한다.
    else:
      if w1_index < len(w1) and c == w1[w1_index]:
        w1_index += 1
        continue
      elif w2_index < len(w2) and c == w2[w2_index]:
        w2_index += 1
        continue
      else:
        answer = 'no'
        break
  #   print(answer)
  # print()

  print(f'Data set {idx+1}: {answer}')
