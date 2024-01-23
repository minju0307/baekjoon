
def solution(n, times):
    answer = 0
    
    ## 이분 탐색의 범위가 시간 리스트
    ## 최솟값은 1분, 최댓값은 가장 오래 걸리는 심사위원에게 n명이 모두 심사받는 시간 

    left = 1 ## 입국 심사에서 걸리는 최소의 시간 
    right = max(times)*n ## 입국 심사에서 걸리는 최대의 시간 
    
    while left <= right :
        # print()
        # print("***")
        ## 중간값을 임의로 잡는다고 할 때 
        mid = (right+left) // 2
        # print("mid: ", mid)
        
        ## 현재 시간 안에서 심사를 받을 수 있는 인원
        people = 0 ## 심사 받은 사람의  수 
        for time in times:
            people += mid // time 
            ## 심사 받은 사람의 수가 n 명보다 크다면 break
            if people >= n :
                break 
        # print("people: ", people)
        
        ## 심사 받은 인원이 n명보다 같거나 크면, 시간이 충분하다는 의미이므로 더 작은 시간이 가능한지 확인해보기
        ## 현재 값이 최적일 수 있으므로 answer = mid로 넣어주기 
        if people >= n:
            answer = mid 
            right = mid - 1
        
        ## 심사 받은 인원이 n명보다 작다면, 시간이 부족하다는 의미이므로 더 많은 시간이 필요한지 확인해보기
        elif people < n :
            left = mid + 1
        
    return answer

if __name__ == '__main__':
    print(solution(6, [2, 5]))