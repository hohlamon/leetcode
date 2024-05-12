# nums1 = [1,2,3,1]
# nums2 = [1,2,3,4]

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hasher = set()
        for num in nums:
            if num in hasher:
                return True
            hasher.add(num)

        return False

# sol = Solution()
# print(sol.containsDuplicate(nums1))
