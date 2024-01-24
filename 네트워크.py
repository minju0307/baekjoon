def find_parent(parent, x):
    if parent[x] != x:
        find_parent(parent, parent[x])
    return parent[x]

def union (parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(n, computers):
    
    ## 부모 테이블을 자기 자신으로 초기화 
    parent = [i for i in range(n)]
    
    ## edge가 연결되어 있으면 union 연산을 수행 
    for i, computer in enumerate(computers):
        # print()
        # print(f"***{i}***")
        for j, edge in enumerate(computer):
            # print(j)
            if i==j:
                continue
            elif edge == 1 :
                union(parent, i, j)
    
    # print(parent)
    answer = len(list(set(parent)))
    
    return answer

if __name__ == '__main__':
    print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))