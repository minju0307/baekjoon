from collections import defaultdict
from itertools import combinations

def solution(clothes):
    answer = 0
    
    dic = defaultdict(int)
    for n, t in clothes:
        dic[t] += 1
        
    types = list(dic.keys())
    
    for i in range(1, len(types)+1):
        comb = combinations(types, i) 

        for tup in list(comb):
            # print(tup)
            if i == 1:
                answer += dic[tup[0]]
            else:
                tmp = 1
                for sub in tup:
                    tmp *= dic[sub]
                answer += tmp 
            # print(answer)

    return answer

if __name__=='__main__':
    solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])