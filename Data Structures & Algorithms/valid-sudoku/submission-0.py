class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for row_idx in range(9):
            for col_idx in range(9):
                cell = board[row_idx][col_idx]

                if cell == '.':
                    continue
                
                if cell in rows[row_idx]:
                    return False
                else:
                    rows[row_idx].add(cell)
                
                if cell in cols[col_idx]: 
                    return False
                else:
                    cols[col_idx].add(cell)
                
                box_idx = 3 * int(row_idx / 3) + int(col_idx / 3)

                if cell in boxes[box_idx]:
                    return False
                else:
                    boxes[box_idx].add(cell)

        return True