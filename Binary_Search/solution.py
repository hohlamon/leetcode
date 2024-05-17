class Solution:
    def iterate(self, nums: list[int], target: int, slice: tuple):
        if (slice[1] - slice[0] == 0):
            if nums[slice[0]] == target:
                return slice[0]
            else:
                return -1

        if nums[slice[0]] == target:
            return slice[0]
        length_slice = slice[1] - slice[0] + 1
        left_slice = (slice[0], slice[0] + (length_slice //2)-1)
        right_slice = (slice[0] + length_slice // 2, slice[1])

        if nums[left_slice[1]] == target:
            return left_slice[1]
        if nums[right_slice[0]] == target:
            return right_slice[0]
        
        if nums[right_slice[0]] < target:
            slice = right_slice
        else:
            slice = left_slice
        return  self.iterate(nums, target, slice)


    def search(self, nums: list[int], target: int) -> int:
        start_slice = (0, len(nums) - 1)
        return self.iterate(nums, target, start_slice)









nums = [-1,0,3,5,9, 12, 13]
test_target = 13

sol = Solution()
print(sol.search(nums, test_target))
