from collections import defaultdict

def solution(phone_book):
    answer = True 
    
    ## dict에다가 모든 접두사의 가능성을 카운트하고, 전화번호부의 숫자가 개수가 2 이상이면 올리기 
    dic = defaultdict(int)
    for num in phone_book:
        for i in range(1, len(num)+1):
            dic[num[:i]] += 1
    for num in phone_book:
        if dic[num] > 1:
            answer = False
        
    return answer