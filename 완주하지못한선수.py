

def solution(participant, completion):
    
    for name in participant:
        if name in completion:
            completion.remove(name)
        else:
            return name