class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 -1
        INT_MIN = -2**31

        if divisor == 0:
            raise ZeroDivisionError
        if not (-2**31 <= dividend <= 2**31 - 1) or not (-2**31 <= divisor <= 2**31 - 1):
            raise ValueError

        
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        else:
            result = dividend / divisor
            if result < -2**31:
                return -2**31
            elif result > 2**31 - 1:
                return 2**31 - 1
            else:
                return int(result)