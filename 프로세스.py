import heapq

def solution(priorities, location):
    
    ## 우선순위 큐를 힙으로 구현 
    hq = []
    
    ## heapq에 push (linear time)
    for idx, value in enumerate(priorities):
        heapq.heappush(hq, (-value, idx))
    
    ## heapq pop
    answer = 1
    while heapq:
        v, i = heapq.heappop(hq)
        if i == location:
            return answer
        answer += 1
        
    return answer