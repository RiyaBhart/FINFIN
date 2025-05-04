import copy

EMPTY = '.'
WHITE = 'W'
BLACK = 'B'
ROWS, COLS = 8, 8

def create_board():
    board = [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]
    for r in range(3):
        for c in range(COLS):
            if (r + c) % 2 == 1:
                board[r][c] = BLACK
    for r in range(5, 8):
        for c in range(COLS):
            if (r + c) % 2 == 1:
                board[r][c] = WHITE
    return board

def print_board(board):
    print("  " + " ".join(map(str, range(COLS))))
    for i, row in enumerate(board):
        print(i, " ".join(row))

def get_moves(board, player):
    direction = -1 if player == WHITE else 1
    moves = []
    captures = []
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == player:
                for dc in [-1, 1]:
                    nr, nc = r + direction, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] == EMPTY:
                        moves.append(((r, c), (nr, nc)))
                    nr2, nc2 = r + 2*direction, c + 2*dc
                    if 0 <= nr2 < ROWS and 0 <= nc2 < COLS:
                        if board[nr][nc] == (BLACK if player == WHITE else WHITE) and board[nr2][nc2] == EMPTY:
                            captures.append(((r, c), (nr2, nc2)))
    return captures if captures else moves

def apply_move(board, move):
    (r1, c1), (r2, c2) = move
    piece = board[r1][c1]
    new_board = copy.deepcopy(board)
    new_board[r1][c1] = EMPTY
    new_board[r2][c2] = piece
    if abs(r2 - r1) == 2:
        new_board[(r1 + r2)//2][(c1 + c2)//2] = EMPTY
    return new_board

def evaluate(board):
    white_count = sum(row.count(WHITE) for row in board)
    black_count = sum(row.count(BLACK) for row in board)
    return black_count - white_count

def minimax(board, depth, alpha, beta, maximizing):
    current_player = BLACK if maximizing else WHITE
    moves = get_moves(board, current_player)
    if depth == 0 or not moves:
        return evaluate(board), None
    best_move = None
    if maximizing:
        max_eval = float('-inf')
        for move in moves:
            result = apply_move(board, move)
            eval_score, _ = minimax(result, depth - 1, alpha, beta, False)
            if eval_score > max_eval:
                max_eval = eval_score
                best_move = move
            alpha = max(alpha, eval_score)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = float('inf')
        for move in moves:
            result = apply_move(board, move)
            eval_score, _ = minimax(result, depth - 1, alpha, beta, True)
            if eval_score < min_eval:
                min_eval = eval_score
                best_move = move
            beta = min(beta, eval_score)
            if beta <= alpha:
                break
        return min_eval, best_move

def is_game_over(board):
    return not get_moves(board, WHITE) or not get_moves(board, BLACK)

def main():
    board = create_board()
    print_board(board)
    while not is_game_over(board):
        print("\nYour move (W):")
        moves = get_moves(board, WHITE)
        if not moves:
            print("No moves available. You lose!")
            break
        for i, move in enumerate(moves):
            print(f"{i}: {move}")
        try:
            choice = int(input("Select move index: "))
            if choice < 0 or choice >= len(moves):
                print("Invalid move index! Try again.")
                continue
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue
        move = moves[choice]
        board = apply_move(board, move)
        print(f"Player moves: {move[0]} → {move[1]}")
        print_board(board)
        if is_game_over(board):
            break
        print("\nAI's move (B):")
        _, ai_move = minimax(board, 4, float('-inf'), float('inf'), True)
        if ai_move:
            board = apply_move(board, ai_move)
            print(f"AI moves: {ai_move[0]} → {ai_move[1]}")
            print_board(board)
        else:
            print("AI cannot move. You win!")
            break
    white_pieces = sum(row.count(WHITE) for row in board)
    black_pieces = sum(row.count(BLACK) for row in board)
    if white_pieces == 0:
        print("You lost. All your pieces are gone.")
    elif black_pieces == 0:
        print("You won! AI has no pieces left.")
    else:
        if not get_moves(board, WHITE):
            print("No moves available for you. You lost!")
        elif not get_moves(board, BLACK):
            print("No moves available for AI. You won!")
        else:
            print("Game over — draw or no legal moves left.")

main()