class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 当前0的数量
        pre_count_0 = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i - pre_count_0] = nums[i]
            else:
                pre_count_0 += 1
        if pre_count_0 != 0:
            nums[-pre_count_0:] = [0] * j
