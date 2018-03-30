class Solution:
    def topKFrequent(self,nums, k):

        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        return [i[0] for i in sorted(d.items(), key=lambda x: x[1], reverse=True)[:k]]