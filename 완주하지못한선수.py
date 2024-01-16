## hash 는 dictionary를 사용하는 알고리즘 
## for 문을 돌면서 in / not in 을 쓰는 것은 사실상 이중 for문 처럼 될 수 있음 
## linear 하게 두 개를 더하는 방식으로 가는 것이 필요 

from collections import defaultdict

def solution(participant, completion):
    
    hash = defaultdict(int)
    
    for name in participant:
        hash[name] +=1
        
    for name in completion:
        if hash[name] > 1:
            hash[name] -= 1
        else:
            del hash[name]

    return list(hash.keys())[0]