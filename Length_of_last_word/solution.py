test_str = '   fly me   to   the moon  '

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.strip().split(" ")
        return len(words[-1])

sol = Solution()
print(sol.lengthOfLastWord(test_str))
