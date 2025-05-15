board = [' '] * 9

def print_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def check_winner(p):
    wins = [(0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6)]
    return any(board[a]==board[b]==board[c]==p for a,b,c in wins)

player = 'X'
for _ in range(9):
    print_board()
    move = int(input(f"Player {player}, enter position (1-9): ")) - 1
    if board[move] != ' ':
        print("Invalid move!")
        continue
    board[move] = player
    if check_winner(player):
        print_board()
        print(f"Player {player} wins!")
        break
    player = 'O' if player == 'X' else 'X'
else:
    print_board()
    print("It's a draw!")
