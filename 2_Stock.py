class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_bp = []
        min_val = prices[0]
        for i in range(len(prices)):
            min_val = min(min_val, prices[i])
            min_bp.append(min_val)

        for i in range(len(prices)):
            min_bp[i] = prices[i] - min_bp[i]

        return max(min_bp)