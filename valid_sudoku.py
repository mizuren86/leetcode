class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxes = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num != '.':
                    box_index = (r // 3) * 3 + (c // 3)

                    if (num in rows[r]) or (num in cols[c]) or (num in boxes[box_index]):
                        return False

                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box_index].add(num)

        return True
   
            