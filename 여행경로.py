def solution(tickets):
    routes = {} ## key: 시작지점, value: 도착 지점 / 갈 수 있는 공항이 있는지 없는지 확인하기 위하여 / 중복 경로도 구분이 됨 
    for t in tickets:
        routes[t[0]] = routes.get(t[0], []) + [t[1]]
        
    for r in routes:
        routes[r].sort(reverse=True) ## 도착 지점들은 알파벳 거꾸로 순서로 정렬 
        
    stack = ["ICN"]
    path = []
    
    while len(stack) > 0:
        print("***")
        print("routes:", routes)
        print("stack:", stack)
        print("path:", path)
        print()
        top = stack[-1]
        
        if top not in routes or len(routes[top]) == 0: ## 모든 루트를 잘 따라 갔을 때  / 혹은 길을 찾던 도중 더이상 갈 수 있는 공항이 없을 때 
            path.append(stack.pop()) ## stack에서 지우기 / path에 경로를 추가하기 
        else:
            stack.append(routes[top][-1]) ## 다음에 갈 수 있는 공항 중 알파벳이 빠른 순서를 stack에 넣기 
            routes[top] = routes[top][:-1] ## stack에 넣은 공항은 routes에서 제거하기 
    
    return path[::-1]

if __name__=="__main__":
    print(solution([["ICN", "AAA"], ["ICN", "CCC"], ["CCC", "DDD"], ["AAA", "BBB"], ["AAA", "BBB"], ["DDD", "ICN"], ["BBB", "AAA"]]))