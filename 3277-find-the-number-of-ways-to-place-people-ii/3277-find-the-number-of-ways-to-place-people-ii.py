class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        
        points.sort(key=lambda p: (p[0], -p[1]))
        
        n = len(points)
        ans = 0

        for i in range(n):
            max_y = float("-inf")  # track lowest Bob candidate y so far
            for j in range(i + 1, n):
                # Alice must be upper-left of Bob
                if points[i][1] >= points[j][1]:
                    if points[j][1] > max_y:  # no blocker inside rectangle
                        ans += 1
                        max_y = points[j][1]
        return ans