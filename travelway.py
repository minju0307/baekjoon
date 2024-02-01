def dfs(graph, visited, path, current):
    path.append(current)        # 현재까지 방문한 공항 경로
    if len(path) == sum(len(dests) for dests in graph.values()) + 1:
        return path          # 모든 항공권 사용했을 때만 참으로 종료
    if current in graph:
        for i, next_dest in enumerate(graph[current]):
            if not visited[current][i]:            # 모든 항공권 순회하면서, 사용하지 않은 항공권 찾아
                visited[current][i] = True
                result = dfs(graph, visited, path, next_dest)      # 다음 목적지로 이동
                if result:
                    return result
                visited[current][i] = False         # 유효한 경로 못 찾으면 백트래킹
    path.pop()                                      # 백트래킹을 위해 path에서 pop
    return None

def solution(tickets):
    graph = {}         # 도착 항공권
    visited = {}       # 항공권 사용 여부
    for d, a in tickets:
        if d not in graph:
            graph[d] = []
            visited[d] = []
        graph[d].append(a)
        visited[d].append(False)    # 항공권 사용 여부 초기화
    for d in graph.keys():
        graph[d].sort()             # 알파벳 순 정렬
    return dfs(graph, visited, [], "ICN")