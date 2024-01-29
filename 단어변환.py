
from collections import deque 
            
def solution(begin, target, words):
    
    words.append(target)
    words = list(set(words))
    words = [(idx+1, w) for idx, w in enumerate(words)]
    
    print(words)
    print(begin)
    print(target)
    
    visited = [0]*(len(words)+1)
    
    queue = deque([(0, begin)])
    visited[0] = 1
    distance = 0
    answer = 0
    
    while queue:
        print()
        print(queue)
        current = queue.popleft()
        
        if current == target:
            break
        
        for w_idx, w in words:
            ## 이미 방문 했던 단어는 넘어가기 / 자기 자신도 넘어가게 됨 
            if visited[w_idx] == 1 :
                continue
            
            ## current 에서 한 글자 바꿔서 변경 가능한 애들은 큐에 추가하기 
            correct = 0
            wrong = 0
            for iidx, i in enumerate(list(w)):
                if i == current[1][iidx]:
                    correct += 1
                else:
                    wrong += 1
            
            if correct == len(current[1])-1 and wrong == 1:
                queue.append((w_idx, w))
                visited[w_idx] = 1
    

    return answer

if __name__ == "__main__":
    solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])