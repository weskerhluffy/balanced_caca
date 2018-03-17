def isBalanced(s):
    fail=False
    opening_braces = {'{', '[', '('}
    
    matching_braces = {'}':'{', ']':'[', ')':'('}
    
    stack = []
    
    for c in s:
        if c in opening_braces:
            stack.append(c)
        else:
            if not stack:
                fail=True
                break
            mb = stack.pop()
            if matching_braces[c] != mb:
                fail=True
                break
    if not fail and not stack:
        print(1)
    else:
        print(2)
#    return "YES" if not fail and not stack else "NO"
