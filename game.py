import itertools
import numpy as np

# blocks = np.array([
#     [2, 4, 3, 4, 2, 9, 2, 7, 2],
#     [9, 5, 9, 3, 5, 4, 5, 1, 6],
#     [8, 3, 2, 6, 9, 2, 1, 8, 3]
# ])

# for i in range(len(blocks[0])):
#     for j in range(len(blocks[1])):
#         # Horizontal
#         if i + 1 < len(blocks[0]) and j + 1 < len(blocks[1]):
#             if blocks[i][j] == blocks[i][j+1]:
#                 print(i, j, j+1)

#         # Vertical
#         if i + 1 < len(blocks[0]) and j + 1 < len(blocks[1]):
#             if blocks[i][j+1] == blocks[i+1][j]:
#                 print(i, i+1, j)

#         # Next Line


#         # Diagonal


#         ...

# Sudoku problem
board = np.array(
    [
        [0, 0, 2, 0, 8, 0, 0, 5, 0],
        [0, 5, 6, 9, 1, 7, 0, 3, 0],
        [0, 4, 0, 0, 5, 0, 8, 7, 1],
        [0, 9, 0, 0, 0, 0, 6, 0, 0],
        [6, 7, 1, 0, 9, 5, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [1, 6, 7, 0, 3, 0, 5, 9, 0],
        [4, 8, 0, 0, 7, 0, 3, 0, 0],
        [0, 2, 5, 4, 6, 0, 0, 0, 0],
    ]
)


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(f"{str(bo[i][j])} ", end="")


def find_empty(bo):
    return next(
       (
           (i, j)
           for i, j in itertools.product(range(len(bo)), range(len(bo[0])))
           if bo[i][j] == 0
       ),
       None,
    )

def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    
    return not any(
        bo[i][j] == num and (i, j) != pos
        for i, j in itertools.product(
           range(box_y * 3, box_y * 3 + 3), 
           range(box_x * 3, box_x * 3 + 3)
        )
    )

def solve(bo):
    if find := find_empty(bo):
        row, col = find
    else:
        return True

    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False

print_board(board)
solve(board)
print("___________________")
print_board(board)
