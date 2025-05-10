b = [' '] * 9

def p(): print(f"{b[0]}|{b[1]}|{b[2]}\n-+-+-\n{b[3]}|{b[4]}|{b[5]}\n-+-+-\n{b[6]}|{b[7]}|{b[8]}")

def w(s): return any(b[i]==b[j]==b[k]==s for i,j,k in [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)])

def mm(t):
    if w('O'): return 1
    if w('X'): return -1
    if ' ' not in b: return 0
    scores = []
    for i in range(9):
        if b[i] == ' ':
            b[i] = 'O' if t else 'X'
            scores.append(mm(not t))
            b[i] = ' '
    return max(scores) if t else min(scores)

while True:
    p()
    m = int(input("Move (1-9): ")) - 1
    if b[m] != ' ': continue
    b[m] = 'X'
    if w('X'): p(); print("You win!"); break
    if ' ' not in b: p(); print("Draw!"); break
    best = -1e9
    for i in range(9):
        if b[i] == ' ':
            b[i] = 'O'
            score = mm(False)
            b[i] = ' '
            if score > best:
                best, move = score, i
    b[move] = 'O'
    if w('O'): p(); print("Computer wins!"); break
    if ' ' not in b: p(); print("Draw!"); break
