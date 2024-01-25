def solution(nums):
    answer = 0
    n = len(nums)
    answer += len(set(nums))
    if answer > n//2:
        answer = n//2
    return answer