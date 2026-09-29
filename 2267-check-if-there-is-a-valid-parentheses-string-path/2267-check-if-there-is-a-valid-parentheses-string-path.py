class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        rows=len(grid)
        cols=len(grid[0])
        # the valid parenthesis always a even length so we need to check this
        if (rows+cols-1)%2:
            return False
        memo = {}
        def dfs(r,c,balance):
            if r>=rows or c>=cols:
                return False
            
            balance += 1 if grid[r][c]=="(" else -1
            if balance < 0 :
                return False # means we have only ))) like this if is never to be valid
            if(r,c,balance) in memo:
                return memo[(r,c,balance)]

            remaining = rows -1 -r + cols - c - 1
            if balance > remaining:
                return False
            """
            How many cells are left to visit after the current cell?
            Example

            Suppose:

            grid = 4 x 4

            Coordinates are:

            (0,0) (0,1) (0,2) (0,3)
            (1,0) (1,1) (1,2) (1,3)
            (2,0) (2,1) (2,2) (2,3)
            (3,0) (3,1) (3,2) (3,3)

            Imagine you're currently at:

            (r, c) = (1, 2)

            You need to reach:

            (3, 3)
            How many moves are required?

            From row 1 to row 3:

            3 - 1 = 2 down moves

            From column 2 to column 3:

            3 - 2 = 1 right move

            Therefore:

            2 + 1 = 3 moves

            That's exactly what this calculates:

            (rows - 1 - r) + (cols - 1 - c)

            = (4 - 1 - 1) + (4 - 1 - 2)
            = 2 + 1
            = 3

            So:

            remaining = 3
            Why do we need this?

            Suppose your current balance is:

            balance = 5

            You have only:

            remaining = 3

            cells/moves left.

            Even if all three remaining cells are:

            )
            )
            )

            your balance becomes:

            5 → 4 → 3 → 2

            You cannot reach 0.
            
            
            """
            if r==rows-1 and c==cols-1:
                
                return balance==0
            

            down = dfs(r+1,c,balance)
            right = dfs(r,c+1,balance)
            memo[(r,c,balance)] = down or right
            return memo[(r,c,balance)]
        return dfs(0,0,0)