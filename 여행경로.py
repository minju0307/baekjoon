
def dfs(d, a, idx, visited, tickets, answer):
    
    ## 종료 조건 
    if 0 not in visited:
        answer.append(a)
        if (len(answer) == len(tickets)+1): ## 모든 티켓이 사용되었고, 모든 공항을 방문했다면 
            ans.append(answer)
            return
    
    ## 다음 지점 후보 선택
    for new_idx, (new_d, new_a) in enumerate(tickets): 
        if visited[new_idx] == 1: continue
        if a == new_d:
            answer.append(new_d)
            visited[new_idx]=1
            dfs(new_d, new_a, new_idx, visited, tickets, answer)
            visited[new_idx]=0
            answer=answer[:-1]

def solution(tickets):
    global ans
    
    ans = []
    for idx, (d, a) in enumerate(tickets): ## 시작 지점 후보 선택
        if d == "ICN":
            answer = []
            answer.append("ICN")
            visited = [0] * len(tickets) ## 항공권을 사용했는지 확인
            visited[idx] = 1
            dfs(tickets[idx][0], tickets[idx][1], idx, visited, tickets, answer)
            visited[idx]=0
    return min(ans)

if __name__=="__main__":
    print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))