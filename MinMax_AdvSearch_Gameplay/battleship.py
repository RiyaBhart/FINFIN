import random

GRID_SIZE = 10
SHIP_SIZES = [3, 2]

def create_grid():
    return [['~' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

def display_grid(grid):
    print("  " + " ".join(str(i+1) for i in range(GRID_SIZE)))
    for idx, row in enumerate(grid):
        print(chr(65 + idx), " ".join(row))

def place_ship(grid, size):
    while True:
        direction = random.choice(['H', 'V'])
        if direction == 'H':
            row = random.randint(0, GRID_SIZE-1)
            col = random.randint(0, GRID_SIZE-size)
            if all(grid[row][col+i] == '~' for i in range(size)):
                for i in range(size):
                    grid[row][col+i] = 'S'
                break
        else:
            row = random.randint(0, GRID_SIZE-size)
            col = random.randint(0, GRID_SIZE-1)
            if all(grid[row+i][col] == '~' for i in range(size)):
                for i in range(size):
                    grid[row+i][col] = 'S'
                break

def setup_board(grid):
    for size in SHIP_SIZES:
        place_ship(grid, size)

def parse_input(coord):
    try:
        row = ord(coord[0].upper()) - 65
        col = int(coord[1:]) - 1
        if 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE:
            return row, col
    except:
        return None
    return None

def all_ships_sunk(grid):
    return all(cell != 'S' for row in grid for cell in row)

def adjacent_cells(r, c):
    moves = [(-1,0), (1,0), (0,-1), (0,1)]
    neighbors = []
    for dr, dc in moves:
        nr, nc = r + dr, c + dc
        if 0 <= nr < GRID_SIZE and 0 <= nc < GRID_SIZE:
            neighbors.append((nr, nc))
    return neighbors

player_board = create_grid()
ai_board = create_grid()
ai_mask = create_grid()

setup_board(player_board)
setup_board(ai_board)

ai_targets = []
ai_memory = set()

print("Welcome to Battleship!")
print("Try to sink the AI ships!")

while True:
    print("\nYour Turn:")
    display_grid(ai_mask)
    move = input("Enter coordinate (e.g., B4): ").strip().upper()
    pos = parse_input(move)
    if not pos:
        print("Invalid input.")
        continue
    r, c = pos
    if ai_mask[r][c] != '~':
        print("Already attacked here.")
        continue
    if ai_board[r][c] == 'S':
        ai_mask[r][c] = 'X'
        ai_board[r][c] = 'X'
        print(f"You hit at {move}!")
    else:
        ai_mask[r][c] = 'O'
        print(f"You missed at {move}.")

    if all_ships_sunk(ai_board):
        print("Victory! You sank all AI ships.")
        break

    print("\nAI's Turn:")
    if ai_targets:
        r, c = ai_targets.pop(0)
    else:
        while True:
            r, c = random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1)
            if (r, c) not in ai_memory:
                break
    ai_memory.add((r, c))
    if player_board[r][c] == 'S':
        player_board[r][c] = 'X'
        print(f"AI hits at {chr(65+r)}{c+1}!")
        ai_targets.extend(cell for cell in adjacent_cells(r, c) if cell not in ai_memory)
    else:
        print(f"AI misses at {chr(65+r)}{c+1}.")

    if all_ships_sunk(player_board):
        print("Defeat! AI sank all your ships.")
        break