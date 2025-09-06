class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:

        def getops(n: int) -> int:
            res = 0
            ops = 0
            pof = 1

            while pof <= n:

                left = pof
                right = min(n, pof * 4 - 1)
                ops += 1
                res += (right - left + 1) * ops
                pof *= 4

            return res
        
        return sum(
            (getops(r) - getops(l - 1) + 1) // 2
            for l, r in queries
        )