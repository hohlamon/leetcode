class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = set(s + t)
        for letter in letters:
            if s.count(letter) != t.count(letter):
                return False

        return True

# test1 = 'lol'
# test2 = 'lolkek'

# sol = Solution()
# print(sol.isAnagram(test1, test2))
