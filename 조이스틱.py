## 정답 코드 참고: https://velog.io/@jqdjhy/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%A1%B0%EC%9D%B4%EC%8A%A4%ED%8B%B1-Greedy
## 그리디로 그때그때 짧게 갈 경우 틀리게 해석되는 경우가 있음. 전체적인 상황을 고려하여 어떻게 가는게 최소 이동인지 구하는 것이 핵심

def solution(name):
    answer = 0
    min_move = len(name) - 1 ## 최대 이동 횟수로 초기화 
    
    for i, char in enumerate(name):
        ## 최소 알파벳 변경 횟수 (위아래)
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        
        ## 다음 문자열에 A가 오래 있는 경우 
        ## 제일 긴 문자열의 개수를 찾아야 함 
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        
        ## 최소 이동 횟수 구하기 -> 여기서는 현재 위치와는 상관 없이 전체 이동 횟수를 구함 
        
        # print(char)
        # print(min_move)
        # print(2*i + len(name) - next)
        # print(i + 2*(len(name) -next))
        # print()
        
        ## 2*i + len(name) - next : 연속된 A의 왼쪽으로 커서를 옮긴 다음에, 왼쪽 방향으로 쭉 훑는 경우 (연속된 A의 왼쪽이 짧을 경우 효과적)
        ## 2*(len(name) -next : 연속된 A의 오른쪽으로 커서를 옮긴 다음에, 오른쪽 방향으로 쭉 훑는 경우 (연속된 A의 오른쪽이 짧을 경우 효과적)
        min_move = min([min_move, 2*i + len(name) - next, i + 2*(len(name) -next)])
        
    answer += min_move
    return answer

if __name__ =="__main__":
    name="NOTBAAAAD"
    print(solution(name))