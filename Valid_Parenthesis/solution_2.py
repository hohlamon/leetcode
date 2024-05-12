class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = set('({[')
        
        for sym in s:
            if sym in opening:
                stack.append(sym)
            else:
                if not stack:
                    return False
                else:
                    last_sym = stack.pop()
                if sym == ')' and last_sym != '(':
                    return False
                if sym == ']' and last_sym != '[':
                    return False
                if sym == '}' and last_sym != '{':
                    return False
        if stack:
            return False
        return True
