class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        cache = {}
        def rec(i, bought, cache):
            if i == len(prices):
                return 0
            if (i, bought) in cache:
                return cache[(i, bought)]
            res = rec(i+1, bought, cache)
            if bought:
                res = max(res, prices[i] + rec(i+1, False, cache))
            else:
                res = max(res, -prices[i] + rec(i+1, True, cache))
            cache[(i, bought)] = res
            return res
        return rec(0, False, cache)