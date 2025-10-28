import time
import os

def clear_screen():
    """Clear the console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_grid(grid):
    """Display the Sudoku grid with borders"""
    print("+" + "---+"*4)
    for i, row in enumerate(grid):
        print("|", end="")
        for j, num in enumerate(row):
            print(f" {num if num != 0 else ' '} |", end="")
        print()
        print("+" + "---+"*4)
    print("\n")

def is_valid(grid, row, col, num):
    """Check if placing num at grid[row][col] is valid"""
    for x in range(4):
        if grid[row][x] == num:
            return False
    for y in range(4):
        if grid[y][col] == num:
            return False
    start_row = row - row % 2
    start_col = col - col % 2
    for i in range(2):
        for j in range(2):
            if grid[start_row + i][start_col + j] == num:
                return False
    return True

def solve_sudoku(grid):
    """Solve 4x4 Sudoku with backtracking and step-by-step UI"""
    for row in range(4):
        for col in range(4):
            if grid[row][col] == 0:
                for num in range(1, 5):
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num
                        clear_screen()
                        print("Solving Sudoku...\n")
                        print_grid(grid)
                        time.sleep(0.3)  # pause to show steps
                        if solve_sudoku(grid):
                            return True
                        grid[row][col] = 0  # Backtrack
                        clear_screen()
                        print("Backtracking...\n")
                        print_grid(grid)
                        time.sleep(0.3)
                return False
    return True
