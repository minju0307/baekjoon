from collections import defaultdict
from itertools import combinations

def solution(clothes):
    
    dic = defaultdict(int)
    for _, t in clothes:
        dic[t] += 1
        
    answer = sum(list(dic.values()))
    types = list(dic.keys())
    
    for i in range(2, len(types)+1):
        comb = combinations(types, i) 

        for tup in list(comb):
            tmp = 1
            for sub in tup:
                tmp *= dic[sub]
            answer += tmp 
            
    return answer

if __name__=='__main__':
    solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])