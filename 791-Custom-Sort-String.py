class Solution:
    def customSortString(self, order: str, s: str) -> str:
        order_map = {char: index for index, char in enumerate(order)}
        sorted_s = sorted(s, key=lambda char: order_map.get(char, len(order)))

        return ''.join(sorted_s)
