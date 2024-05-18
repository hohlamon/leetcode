class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_diff = 0
        minimal = prices[0]
        for num in prices:
            if minimal > num:
                minimal = num
                continue
            temp_diff = num - minimal
            if temp_diff > max_diff:
                max_diff = temp_diff

        return max_diff


# test = [7,1,5,3,6,4]
# sol = Solution()
# print(sol.maxProfit(test))