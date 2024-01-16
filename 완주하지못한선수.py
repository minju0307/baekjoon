

def solution(participant, completion):
    
    score = [0 for _ in range(len(participant))]
    
    for idx, name in enumerate(participant):
        if name in completion:
            score[idx] += 1
            completion.remove(name)
    
    answer = participant[score.index(0)]
    
    
    return answer