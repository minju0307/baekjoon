from collections import deque

def solution(maps):
    
    ## 상대방이 있는 위치 
    n = len(maps)-1
    m = len(maps[0])-1
    
    ## 동서남북 이동을 정의
    dx = [0, 0, 1, -1] ## 행
    dy = [1, -1, 0, 0] ## 열 
    
    ## bfs를 위한 queue 초기화 
    queue=deque([(0,0)])
    
    while queue:
        x, y = queue.popleft() ## 현재 위치
        
        # print("***")
        # print(x, y)
        # print(maps[x][y])
        
        ## 동서 남북으로 이동하기 
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            
            ## 맵을 벗어난 경우는 무시하기 
            if nx < 0 or nx > n or ny < 0 or ny > m:
                continue
            
            ## 벽인 경우는 무시하기
            if maps[nx][ny] == 0:
                continue
            
            ## 갈 수 있는 경우에는 큐에 넣고 최단경로를 기록하기 (이미 방문한 경우는 고려하지 않기)
            if maps[nx][ny] == 1:
                queue.append((nx, ny))
                maps[nx][ny] += maps[x][y]
        
    if maps[n][m] > 1:
        answer = maps[n][m]
    else:
        answer = -1 
        
    return answer

if __name__=="__main__":
    maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
    
    for line in maps:
        print(line)
    print()
    
    print(solution(maps))