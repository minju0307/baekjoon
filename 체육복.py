
def solution(n, lost, reserve):
    answer = 0
    
    ## 빌려줄 수 있는 학생과 받아야 하는 학생 정리 
    both = list(set(lost).intersection(set(reserve)))
    lost = [i for i in lost if i not in both ]
    reserve = [i for i in reserve if i not in both ]
    
    answer = n - len(lost)
    
    ## 체육복을 빌려줄 수 있는 학생 찾기 
    for i in lost:
        if i-1 in reserve:
            reserve.remove(i-1)
            answer += 1
            continue
        if i+1 in reserve:
            reserve.remove(i+1)
            answer +=1 
        
    return answer

if __name__ == "__main__":
    n = 5
    lost = [2,4]
    reserve = [1,3,5]
    print(solution(n,lost,reserve))