class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        ans = 0

        points.sort(key=lambda p: (p[0], -p[1]))

        for i in range(len(points)):
            max_y = float("-inf")
            for j in range(i + 1, len(points)):
                if points[i][1] >= points[j][1] and points[j][1] > max_y:
                    ans += 1
                    max_y = points[j][1]
        return ans
