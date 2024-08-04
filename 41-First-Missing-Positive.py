class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.append(0)
        n = len(nums)

        for i in range(n):
            if nums[i] < 0 or nums[i] > n:
                nums[i] = 0
        
        temp = nums[0]
        for i in range(n):
            if nums[i] > 0:
                nums[nums[i]%n-1] +=n
        if nums[0] == temp: return 1

        for i in range(n): 
            if nums[i] // n == 0:
                return i + 1

        return n 
                
        