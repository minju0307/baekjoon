def solution(citations):
    h = 0
    count = 0
    for i in sorted(citations, reverse=True):
        count += 1
        tmp = min(i, count)
        h = max(tmp, h)
        
    return h