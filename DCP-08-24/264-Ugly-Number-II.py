class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1] 
        seen = set(heap)  
        primes = [2, 3, 5]  
        
        for _ in range(n):
            ugly = heapq.heappop(heap)
            
            for prime in primes:
                new_ugly = ugly * prime
                if new_ugly not in seen:
                    heapq.heappush(heap, new_ugly)
                    seen.add(new_ugly)
        
        return ugly  
