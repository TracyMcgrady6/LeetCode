from functools import reduce


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        i = 0
        nums = sorted(nums)
        while i < len(nums):
            if nums[i] == nums[i + 1]:
                i += 2
            else:
                return nums[i]

    def singleNumber_1(self, nums):
        return reduce(lambda x, y: x ^ y, nums)


a = [1, 1, 2, 2, 3]
print(Solution().singleNumber_1(a))
