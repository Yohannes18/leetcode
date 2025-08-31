class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        # convert number to string

        s = str(x)

        return s == s[::-1]