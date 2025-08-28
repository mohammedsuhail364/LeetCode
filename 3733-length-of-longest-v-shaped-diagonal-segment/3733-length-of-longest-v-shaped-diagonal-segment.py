class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])

        @cache
        def search(r, c, target, turn, dir):
            if r < 0 or r >= rows or c < 0 or c >= columns or grid[r][c] != target:
                return 0
            
            target = 0 if target == 2 else 2
            total = 0

            if turn:
                if dir == 'top-left': 
                    total = max(total, search(r - 1, c - 1, target, True, 'top-left') + 1)
                elif dir == 'top-right': 
                    total = max(total, search(r - 1, c + 1, target, True, 'top-right') + 1)
                elif dir == 'bottom-left': 
                    total = max(total, search(r + 1, c - 1, target, True, 'bottom-left') + 1)
                elif dir == 'bottom-right': 
                    total = max(total, search(r + 1, c + 1, target, True, 'bottom-right') + 1)
            else:
                if dir == 'top-left': 
                    total = max(total, search(r - 1, c - 1, target, False, 'top-left') + 1)
                    total = max(total, search(r - 1, c + 1, target, True, 'top-right') + 1)
                elif dir == 'top-right': 
                    total = max(total, search(r - 1, c + 1, target, False, 'top-right') + 1)
                    total = max(total, search(r + 1, c + 1, target, True, 'bottom-right') + 1)
                elif dir == 'bottom-left': 
                    total = max(total, search(r + 1, c - 1, target, False, 'bottom-left') + 1)
                    total = max(total, search(r - 1, c - 1, target, True, 'top-left') + 1)
                elif dir == 'bottom-right': 
                    total = max(total, search(r + 1, c + 1, target, False, 'bottom-right') + 1)
                    total = max(total, search(r + 1, c - 1, target, True, 'bottom-left') + 1)
            
            return total
        
        res = 0
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1:
                    res = max(res, search(r - 1, c - 1, 2, False, 'top-left') + 1)
                    res = max(res, search(r - 1, c + 1, 2, False, 'top-right') + 1)
                    res = max(res, search(r + 1, c - 1, 2, False, 'bottom-left') + 1)
                    res = max(res, search(r + 1, c + 1, 2, False, 'bottom-right') + 1)
        
        return res