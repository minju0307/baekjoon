def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union (parent, i, j):
    ir = find_parent(parent, i)
    jr = find_parent(parent, j)
    if ir < jr:
        parent[jr] = ir
    else:
        parent[ir] = jr

def solution(n, computers):
    
    ## 부모 테이블을 자기 자신으로 초기화 
    parent = [i for i in range(n)]
    
    ## edge가 연결되어 있으면 union 연산을 수행 
    for i, computer in enumerate(computers):
        for j, edge in enumerate(computer):
            if i==j:
                continue
            elif edge == 1:
                union(parent, i, j)
    
    ## 부모 행렬의 root를 찾아내서 정리하는 것이 필요함. 
    for i in range(n):
        parent[i] = find_parent(parent, i)
    
    answer = len(list(set(parent)))
    
    return answer

if __name__ == '__main__':
    print(solution(4, [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]))