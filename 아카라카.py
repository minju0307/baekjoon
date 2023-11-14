import sys

S = sys.stdin.readline().strip()

if len(S) == 1:
  print('AKARAKA')

else:
  prefix = S[:len(S) // 2]
  suffix = S[ (len(S) // 2 + 1 ) :]

  if S == S[::-1] and prefix == prefix [::-1] and suffix == suffix [::-1] :
    print('AKARAKA')
  else:
    print('IPSELENTI')