from sudoku_solver_ui import solve_sudoku, print_grid, clear_screen

# Example 4x4 Sudoku grid (0 = empty)
grid = [
    [1, 0, 0, 4],
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [2, 0, 0, 3]
]

clear_screen()
print("Original Sudoku Grid:")
print_grid(grid)

# Solve Sudoku with visualization
if solve_sudoku(grid):
    print("Sudoku Solved Successfully!\n")
    print_grid(grid)
else:
    print("No solution exists.")
