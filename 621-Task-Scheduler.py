class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}

        for i in tasks:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        lst = sorted(count.values(), reverse = True)
        max_count = lst[0]
        
        i = 0
        counter = 0
        while i < len(lst) and lst[i] == max_count:
            counter += 1
            i += 1

        ret = (max_count - 1) * (n + 1) + counter
        return max(ret, len(tasks))
