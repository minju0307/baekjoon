def solution(numbers, target):
    
    def check(idx, local_hap):
        nonlocal answer
    
        if idx == len(numbers):
            if local_hap == target:
                answer += 1
            return 
    
        check(idx+1, local_hap+numbers[idx]) ## 더해주는 경우
        check(idx+1, local_hap-numbers[idx]) ## 빼주는 경우 
    
    
    answer = 0 
    check(0, 0)

    return answer