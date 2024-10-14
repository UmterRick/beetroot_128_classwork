game_map = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

def transform_position_into_coords(position):
    positions = {
        7: (0, 0),
        8: (0, 1),
        9: (0, 2),
        4: (1, 0),
        5: (1, 1),
        6: (1, 2),
        1: (2, 0),
        2: (2, 1),
        3: (2, 2),
    }
    return positions[position]



def draw_map():
    """
    Print pretty map
    :return: None
    """
    for row in game_map:
        print(*row, sep=" | ")
        print("-" * 10)



def check_equals(data):
    """
    Util to check all elements in data are the same
    :param data: Iterable
    :return: bool
    """
    if "-" in data:
        return False

    if all(x == data[0] for x in data):
        return True
    return False


def check_rows():
    """
    Iterate through map rows and check if all values in row are the same
    :return:
    """
    for row in game_map:
        if check_equals(row):
            return row[0]

def check_columns():
    columns = [[row[i] for row in game_map] for i in range(len(game_map[0]))]
    for column in columns:
        if check_equals(column):
            return column[0]


def check_diagonals():
    n = len(game_map)
    main_diagonal = [game_map[i][i] for i in range(n)]
    anti_diagonal = [game_map[i][n - 1 - i] for i in range(n)]
    for diagonal in [main_diagonal, anti_diagonal]:
        if check_equals(diagonal):
            return diagonal[0]


def check_winner():
    a = check_columns()
    if a:
        return a
    b = check_rows()
    if b:
        return b
    c = check_diagonals()
    if c:
        return c



def is_empty_cell(coords):
    row, column = coords
    cell_value = game_map[row][column]
    if cell_value != "-":
        return False
    return True


def make_turn(player):
    """
    Get turn info form user
    :return:
    """
    while True:
        position = input(f"Player '{player}' turn: ").strip()
        if position.isdigit():
            position = int(position)
            coords = transform_position_into_coords(position)
            if is_empty_cell(coords):
                row, column = coords
                game_map[row][column] = player
                draw_map()
                break
            else:
                print("This cell is not available")


def switch_player(p):
    if p == 'x':
        return '0'
    if p == '0':
        return 'x'


def play():
    draw_map()
    player = 'x'
    while True:
        make_turn(player)
        winner = check_winner()
        if winner is not None:
            print(f"Player {winner} WINS")
            break
        player = switch_player(player)


play()