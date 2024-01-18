from itertools import combinations

def solution(numbers, target):
    answer = 0
    
    pos = [i for i in range(len(numbers))]
    
    for i in range(1, len(pos)+1):
        pos_idx = list(combinations(pos, i))
        
        ## 개수별 조합에 대하여  
        for j in pos_idx:
            hap = 0
            for k in range(len(numbers)):
                if k in j:
                    hap += numbers[k]
                else:
                    hap -= numbers[k]
            if hap == target:
                answer +=1  
        
    
    return answer