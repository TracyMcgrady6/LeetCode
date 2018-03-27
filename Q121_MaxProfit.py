class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        cur_min = prices[0]
        max_pro = 0
        for i in range(len(prices)):
            if prices[i] < cur_min:
                cur_min = prices[i]
            if max_pro < prices[i] - cur_min:
                max_pro=prices[i] - cur_min

        return max_pro
# p = [7, 1, 5, 3, 6, 4]
# print(Solution().maxProfit(p))
p = [3, 2, 6, 5, 0, 3]
print(Solution().maxProfit(p))
