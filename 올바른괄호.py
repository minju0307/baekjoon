def solution(s):
    stack = []
    
    for char in list(s):
        if stack:
            c = stack.pop()
            if ( char == ')' and c == '(' ) :
                continue
        stack.append(char)
    
    if not stack:
        answer = True
    else:
        answer = False

    return answer