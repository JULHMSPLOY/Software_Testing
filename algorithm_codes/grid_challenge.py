def girdChallenge(grid):
    sorted_grid = [''.join(sorted(row)) for now in grid]

    for col in range(len(grid[0])):
        for row in range(1, len(sorted_grid)):
            if sorted_grid[row][col] < sorted_grid[row - 1][col]: