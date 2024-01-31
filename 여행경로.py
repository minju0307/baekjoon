
def dfs(d, a, idx, visited, tickets, answer):
    print("***")
    print(tickets[idx])
    
    if all(visited):
        answer.append(a)
        if (len(answer) == len(tickets)+1):
            return answer
        else:
            return False
    
    for new_idx, (new_d, new_a) in enumerate(tickets):
        if visited[new_idx] == 1: continue
        if a == new_d:
            print(">>>")
            print(tickets[new_idx])
            print()
            answer.append(new_d)
            visited[new_idx]=1
            return dfs(new_d, new_a, new_idx, visited, tickets, answer)
            

def solution(tickets):
    start_can = []
    ans = []
    for idx, (d, a) in enumerate(tickets): ## 시작 지점 후보 선택
        if d == "ICN":
            start_can.append((a, idx))
    
    for _, idx in sorted(start_can): ## 시작 지점 후보들에 대하여 
        answer = []
        visited = [0] * len(tickets) ## 항공권을 사용했는지 확인 
        answer.append("ICN")
        visited[idx] = 1
        answer = dfs(tickets[idx][0], tickets[idx][1], idx, visited, tickets, answer)
        if answer:
            return answer


if __name__=="__main__":
    print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))