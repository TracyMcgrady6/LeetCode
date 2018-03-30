class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        def adjust_heap(arr, index, length):
            tmp = arr[index]
            k = index * 2 + 1
            while k < length:
                if k + 1 < length and arr[k] < arr[k + 1]:
                    k += 1
                if arr[k] > tmp:
                    arr[index] = arr[k]
                    index = k
                else:
                    break
                k = 2 * k + 1
            arr[index] = tmp

        for i in range(int(len(nums) / 2 - 1), -1, -1):
            adjust_heap(nums, i, len(nums))

        for j in range(len(nums) - 1, -1, -1):

            temp = nums[j]
            nums[j] = nums[0]
            nums[0] = temp
            adjust_heap(nums, 0, j)
            if k + j == len(nums):
                return nums[-k]

    def findKthLargest2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return sorted(nums, reverse=True)[k - 1]
