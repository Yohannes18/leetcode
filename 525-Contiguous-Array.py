class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hashmap = {}
        max_length = 0
        cumulative_sum = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                cumulative_sum -= 1
            else:
                cumulative_sum += 1
            
            if cumulative_sum == 0:
                max_length = i + 1
            elif cumulative_sum in hashmap:
                max_length = max(max_length, i - hashmap[cumulative_sum])
            else:
                hashmap[cumulative_sum] = i
        
        return max_length
        