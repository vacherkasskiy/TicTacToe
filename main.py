CROSS = "X"
ZERO = "O"

# поле. изначально пустое
grid = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

# текущий ход
current_turn = 1

def tprint(string):
    print(string, end="\t")

# сделать ход. поставить символ в ячейку
def make_turn(x, y):

    if grid[x][y] != "-":
        return False

    curr_symbol = CROSS

    if current_turn % 2 == 0:
        curr_symbol = ZERO

    grid[x][y] = curr_symbol

    return True

def print_grid():
    for row in range(4):
        for col in range(4):

            if row == 0 and col == 0:
                tprint(" ")
                continue

            if row == 0:
                tprint(col - 1)
                continue

            if col == 0:
                tprint(row - 1)
        print()

print_grid()