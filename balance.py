def balance_brac(s):
    

    if len(s)%s != 0:
        return False

    opening = set('([{')

    matches = set([('(',')'), ('[', ']'), ('{', '}')])

    stack = []

    for paren in s:
        #if it is an opening parenthesis
        if paren in opening:
            stack.append(paren)
        
        else: #if it is a closing parenthesis:#

            if len(stack) == 0:
                return False

            last_open = stack.pop()

            if (last_open, paren) not in matches:
                return False
                
    return len(stack) == 0

    print(balance_brac(''))
    print(balance_brac('()[]'))
    print(balance_brac('[]({)'))