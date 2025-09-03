class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7

        def pow(base, exp):
            result = 1
            while exp > 0:
                if exp % 2 == 1:
                    result = (result * base) % mod
                base = (base * base) % mod
                exp //= 2
            return result
        evn = (n + 1) // 2
        od = n // 2

        ans = (pow(5, evn) * pow(4, od)) % mod

        return ans