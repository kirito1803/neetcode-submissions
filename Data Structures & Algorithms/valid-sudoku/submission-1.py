class Solution:
    def boxId(self, i: int, j: int) -> int:
        if i < 3:
            if j < 3:
                return 0
            elif j < 6:
                return 1
            else:
                return 2
        elif i < 6:
            if j < 3:
                return 3
            elif j < 6:
                return 4
            else:
                return 5
        else:
            if j < 3:
                return 6
            elif j < 6:
                return 7
            else:
                return 8
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell != ".":
                    if ((cell in rows[i]) or (cell in cols[j]) or (cell in boxes[self.boxId(i, j)])):
                        return False
                    else:
                        rows[i].add(cell)
                        cols[j].add(cell)
                        boxes[self.boxId(i, j)].add(cell)
        return True

