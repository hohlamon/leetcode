class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        
        for i in range(len(strs[0])):
            for string in strs:
                if len(string) > i and string[i] == strs[0][i]:
                    next
                else:
                    return prefix
            prefix+=string[i]
                
        return prefix
