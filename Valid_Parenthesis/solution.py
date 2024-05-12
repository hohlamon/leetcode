class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = set('[({')
        closing_dict = {
            ')': '(',
            ']': '[',
            '}':'{'
        }
        for sym in s:
            if sym in opening:
                stack.append(sym)
            elif not stack:
                return False
            else:
                if stack.pop() != closing_dict[sym]:
                    return False
        if stack:
            return False
        return True


# sol = Solution()
# print(sol.isValid('()'))