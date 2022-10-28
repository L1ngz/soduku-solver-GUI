import numpy as np

class SolveSudoku:
    def __init__(self, grid) -> None:
        self.grid = grid
        self.static_count = 0
    def possible(self,pos,number):
        for i in range(0,9):
            if self.grid[pos[0]][i] == number:
                return False
        for i in range(0,9):
            if self.grid[i][pos[1]] == number:
                return False
        smallGridX = pos[0]//3 * 3
        smallGridY = pos[1]//3 * 3
        for i in range(smallGridX, smallGridX+3):
            for ii in range(smallGridY, smallGridY+3):
                if self.grid[i][ii] == number:
                    return False
        return True
    
    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:
                    return (i, j)  # row, col

        return None

    def solve(self):
        find = self.find_empty()
        if not find:
            return True
        else:
            row,col = find
        for i in range(1,10):
            if self.possible((row,col),i):
                self.grid[row][col] = i
                
                if self.solve():
                    return True
                self.grid[row][col] = 0
        return False


    def get_grid(self):
        return self.grid

    def print_grid(self):
        print(self.grid)
        return
