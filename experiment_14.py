board = [' '] * 9

def print_board():
    for i in range(0, 9, 3):
        print(board[i] + ' | ' + board[i+1] + ' | ' + board[i+2])
        if i < 6: print('--+---+--')

def check_winner(p):
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    return any(board[i]==board[j]==board[k]==p for i,j,k in wins)

def alpha_beta(is_max, alpha, beta):
    if check_winner('O'): return 1
    if check_winner('X'): return -1
    if ' ' not in board: return 0

    if is_max:
        max_eval = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                eval = alpha_beta(False, alpha, beta)
                board[i] = ' '
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                eval = alpha_beta(True, alpha, beta)
                board[i] = ' '
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

def best_move():
    best_val = -float('inf')
    move = 0
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            move_val = alpha_beta(False, -float('inf'), float('inf'))
            board[i] = ' '
            if move_val > best_val:
                best_val = move_val
                move = i
    return move

# Game loop
for _ in range(9):
    print_board()
    m = int(input("Enter your move (1-9): ")) - 1
    if board[m] != ' ':
        print("Invalid move. Try again.")
        continue
    board[m] = 'X'
    if check_winner('X'):
        print_board()
        print("You win!")
        break
    if ' ' not in board:
        print_board()
        print("It's a draw!")
        break
    ai = best_move()
    board[ai] = 'O'
    if check_winner('O'):
        print_board()
        print("Computer wins!")
        break
else:
    print_board()
    print("It's a draw!")
