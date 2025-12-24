CROSS = "X"
ZERO = "O"

# поле. изначально пустое
grid = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

def tprint(string):
    print(string, end="\t")

# сделать ход. поставить символ в ячейку
def make_turn(x, y, current_turn):

    if grid[x][y] != "-":
        return False

    grid[x][y] = get_curr_player_symbol(current_turn)

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
                continue

            tprint(grid[row - 1][col - 1])

        print()

def check_win():

    # vertical
    for row in range(3):
        if grid[row][0] == grid[row][1] == grid[row][2] != "-":
            return True

    # horizontal
    for col in range(3):
        if grid[0][col] == grid[1][col] == grid[2][col] != "-":
            return True

    # diagonal
    if grid[0][0] == grid[1][1] == grid[2][2] != "-":
        return True

    if grid[2][0] == grid[1][1] == grid[0][2] != "-":
        return True

    return False

def get_curr_player_symbol(current_turn):
    return CROSS if current_turn % 2 == 1 else ZERO

def get_coords():
    print("Напишите координаты в формате X Y. Например – 0 0")
    coords_raw = input().split(" ")

    if len(coords_raw) != 2:
        return -1, -1, True

    for coord in coords_raw:
        if not coord.isdigit():
            return -1, -1, True

    return int(coords_raw[0]), int(coords_raw[1]), False

def start_game():

    current_turn = 1

    while current_turn <= 9:

        print_grid()

        print("Сейчас ходят", get_curr_player_symbol(current_turn))

        x, y, err = get_coords()

        if err:
            print("Координаты введены в неверном формате")
            continue

        success = make_turn(x, y, current_turn)

        if not success:
            print("Выбранная ячейка уже занята")
            continue

        if check_win():
            print_grid()
            print("Победили ", get_curr_player_symbol(current_turn))
            return

        current_turn += 1

    print("Ничья")

start_game()