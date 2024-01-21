from collections import deque

def solution(priorities, location):
    
    max_num_list = deque(sorted(priorities, reverse=True))
    queue = deque([(p, i) for i, p in enumerate(priorities)])
    answer = 0 ## 실행 횟수 
    
    print(queue)
    
    while queue:
        max_num = max_num_list.popleft()
        current_value, current_idx = queue.popleft()
        
        print("idx:", current_idx)
        print("current:", current_value)
        print("max:", max_num)
        print()
        
        if current_value == max_num:
            answer += 1
            if current_idx == location:
                return answer
        else:
            max_num_list.appendleft(max_num)
            queue.append((current_value, current_idx))
        
if __name__ == '__main__':
    print(solution([1, 1, 9, 1, 1, 1], 0))