class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i, line in enumerate(board):
            h_map = {}
            for j, c in enumerate(line):

                # Check 3 X 3 boxes for duplicates
                if i % 3 == 0 and j % 3 == 0:
                    b_map = {}
                    for a in range(3):
                        for b in range(3):
                            bc = board[i + a][j + b]
                            if bc == ".": continue
                            if b_map.get(bc, None): return False
                            b_map[bc] = True
                
                # Check vertical lines for duplicates
                if i == 0:
                    v_map = {}
                    for l in board:
                        if l[j] == ".": continue
                        if v_map.get(l[j], None): return False
                        v_map[l[j]] = True

                # Check horizontal lines for duplicates
                if c == ".": continue
                if h_map.get(c, None): return False
                h_map[c] = True

        return True