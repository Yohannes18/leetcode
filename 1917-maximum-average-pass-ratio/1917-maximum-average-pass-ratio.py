class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:

        def gain(p, t):
            return (p + 1) / (t + 1) - (p / t)
        
        rat = [(-gain(p, t), p, t) for p, t in classes]
        heapq.heapify(rat)

        for _ in range(extraStudents):
            g, p, t = heapq.heappop(rat)
            p += 1
            t += 1
            heapq.heappush(rat, (-gain(p, t), p, t))
        
        finalClass = [[p, t] for _, p, t in rat]
        ave = sum(p / t for p, t in finalClass) / len(finalClass)

        return ave


        