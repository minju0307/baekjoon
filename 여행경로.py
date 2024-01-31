from collections import deque

def solution(tickets):
    answer = []
    visited = [0] * len(tickets) ## 항공권을 사용했는지 확인 
    
    queue = deque()
    can = []
    for idx, (d, a) in enumerate(tickets): ## 시작 지점 선택
        if d == "ICN":
            can.append(([d,a], idx))
    can = sorted(can) ## 알파벳이 빠른 순서로 정렬 
    queue.append(can[0][0])
    visited[can[0][1]] = 1
    answer.append("ICN")

    
    while queue:
        # print()
        # print(queue)
        
        c_d, c_a = queue.popleft()
        answer.append(c_a)
        
        
        # if all(visited):
        #     break
        
        can = []
        for idx, (d, a) in enumerate(tickets):
            if visited[idx] == 1: continue ## 사용한 여행 경로는 다시 갈 수 없음 
            if c_a == d:
                can.append(([d, a], idx))
                
        
        ## 가능한 경로가 2개 이상일 경우 알파벳 순서대로 방문
        if can:
            can = sorted(can)
            queue.append(can[0][0])
            visited[can[0][1]] = 1
        
        
    return answer

if __name__=="__main__":
    print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))