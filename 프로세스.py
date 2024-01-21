from collections import deque

def solution(priorities, location):
    
    queue = deque(priorities)
    
    answer = 0
    idx = 0
    n = len(priorities)
    
    while queue:
        max_num = max(queue)
        current = queue.popleft()
        print("idx:", idx)
        print("current:", current)
        print("max:", max_num)
        print()
        if current == max_num:
            answer += 1
            if idx == location:
                return answer
            idx = (idx+1) % n
            continue
        else:
            queue.append(current)
            idx = (idx+1) % n
        
if __name__ == '__main__':
    print(solution([1, 1, 9, 1, 1, 1], 0))