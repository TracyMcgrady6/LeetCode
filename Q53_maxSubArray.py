class Solution:
    """
    @param nums: A list of integers
    @return: An integer denote the sum of maximum subarray
    """

    def maxSubArray(self, nums):
        # write your code here
        if len(nums) == 1:
            return nums[0]
        max_nums = nums[0]
        cur_nums = 0
        for i in range(len(nums)):
            cur_nums += nums[i]
            if max_nums < cur_nums:
                max_nums = cur_nums

            # 前面的和如果已经小于0了，那么加上下一个元素值，肯定是小于下一个元素值
            # 所以如果前面加起来的值小于0了，则舍弃前面的和，从下一位开始继续求和
            if cur_nums < 0:
                cur_nums = 0
        return max_nums

    def maxSubArray2(self, nums):
        max_sum = nums[0]
        cur_sum = nums[0]
        for num in nums:
            cur_sum = max(num, num + cur_sum)
            max_sum = max(cur_sum, max_sum)
        return max_sum


solution = Solution()
print(solution.maxSubArray2([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
