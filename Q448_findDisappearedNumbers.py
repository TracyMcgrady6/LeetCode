class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = [0] + nums
        for i in range(len(nums)):
            index = abs(nums[i])
            nums[index] = -abs(nums[index])
        return [i for i in range(len(nums)) if nums[i] > 0]

    def findDisappearedNumbers2(self, nums):
        """
        这种方法用到了额外空间，虽然简单粗暴，不满足题目要求
        :type nums: List[int]
        :rtype: List[int]
        """
        tmp = set(nums)
        res = []
        for i in range(1, len(nums) + 1):
            if i not in tmp:
                res.append(i)
        return res


test = [4, 3, 2, 7, 8, 2, 3, 1]
so = Solution()
print(so.findDisappearedNumbers(test))
