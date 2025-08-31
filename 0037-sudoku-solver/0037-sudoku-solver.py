class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empties = []

        # Initialize sets and empty cells list
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = board[i][j]
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[(i//3)*3 + j//3].add(num)
                else:
                    empties.append((i, j))

        def backtrack(index=0):
            if index == len(empties):
                return True  # all cells filled

            i, j = empties[index]
            box_index = (i//3)*3 + j//3

            for num in '123456789':
                if num not in rows[i] and num not in cols[j] and num not in boxes[box_index]:
                    board[i][j] = num
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[box_index].add(num)

                    if backtrack(index + 1):
                        return True

                    # undo
                    board[i][j] = '.'
                    rows[i].remove(num)
                    cols[j].remove(num)
                    boxes[box_index].remove(num)

            return False

        backtrack()