class Coordinate():
    def __init__(self, row, col):
        self.row = row
        self.col = col

def get_valid_adjacent_points_inc_diagonals(row, col, grid):
    coords = []
    for i in range(-1,2):
        for j in range(-1,2):
            if i == 0 and j == 0:
                continue
            if row + i >= 0 and row + i < len(grid) and col + j >= 0 and col + j < len(grid[0]):
                coords.append(Coordinate(row + i, col + j))
    return coords