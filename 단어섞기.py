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
  print(f"***{w3}***")
  for c in w3:
    print(c)
    if w1_index < len(w1) and c == w1[w1_index]:
      w1_index += 1
    elif w2_index < len(w2) and c == w2[w2_index]:
      w2_index += 1
    else:
      answer = 'no'
    print(answer)
  print()

  print(f'Data set {idx}: {answer}')
