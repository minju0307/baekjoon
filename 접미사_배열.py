S = input()
s_list = []

for idx in range(len(S)):
  s_list.append(S[idx:])

s_list.sort()
for word in s_list:
  print(word)
  
