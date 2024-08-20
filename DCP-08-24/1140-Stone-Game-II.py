class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        memo = {}

        prefix_sum = [0] * len(piles)
        prefix_sum[-1] = piles[-1]

        for i in range(len(piles) - 2, -1, -1):
            prefix_sum[i] = prefix_sum[i + 1] + piles[i]
        
        def dp(i, m):
            if i + 2 * m >= len(piles):
                return prefix_sum[i]
            
            if (i, m) in memo:
                return memo[(i, m)]
            
            min_opponent_score = float('inf')

            for x in range(1, 2 * m + 1):
                min_opponent_score = min(min_opponent_score, dp(i + x, max(m, x)))

            
            memo[(i, m)] = prefix_sum[i] - min_opponent_score

            return memo[(i, m)]
        return dp(0, 1)

        