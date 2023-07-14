def largest_square(grid):
    ROWS, COLS = len(grid), len(grid[0])
    cache = {}

    def helper(r, c):
        if r < 0 or c < 0 or r >= ROWS or c >= COLS:
            return 0
