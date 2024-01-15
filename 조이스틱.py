
def get_min_updown(letter):
    if ord(letter)-ord("A") <= 13:
        return ord(letter)-ord("A")
    else:
        return abs(ord("Z")-ord(letter)+1)

def solution(name):
    answer = 0
    visited = [0 if i != "A" else -1 for i in name]
    letter_idx = 0
    
    while 0 in visited:
        answer += get_min_updown(name[letter_idx])
        visited[letter_idx] = 1
        # print(visited)
        
        if 0 in visited:
            ## 오른쪽으로 가서 0을 찾기 
            right_idx = letter_idx
            right_count = 0
            while visited[right_idx] != 0:
                right_idx += 1
                if right_idx > len(name)-1:
                    right_idx = 0
                right_count += 1
            
            ## 왼쪽으로 가서 0을 찾기
            left_idx = letter_idx
            left_count = 0
            while visited[left_idx] != 0:
                left_idx -= 1
                if left_idx == -1:
                    left_idx = len(name)-1
                left_count += 1
            
            if right_count < left_count:
                # print("right: ", right_idx)
                answer += right_count
                letter_idx = right_idx
            else:
                # print("left: ", left_idx)
                answer += left_count
                letter_idx = left_idx
            
    return answer

if __name__ =="__main__":
    name="JAN"
    print(solution(name))