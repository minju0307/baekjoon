def solution(s):
    stack = []
    
    for char in list(s):
        if stack:
            c = stack.pop()
            if ( char == ')' and c == '(' ) :
                continue
            else:
                stack.append(c)
        stack.append(char)

    return not(stack)