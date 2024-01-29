from collections import defaultdict

def solution(clothes):
    answer = 1
    dic = defaultdict(int)
    for _, t in clothes:
        dic[t] += 1
    values = list(dic.values())
    
    for v in values:
        answer *= (v+1) 
            
    return answer-1

if __name__=='__main__':
    print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))