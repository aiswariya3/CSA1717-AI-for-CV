def alphabeta(depth, nodeIndex, isMax, scores, alpha, beta, h):
    if depth == h:
        return scores[nodeIndex]

    if isMax:
        best = float('-inf')
        for i in range(2):
            val = alphabeta(depth + 1, nodeIndex * 2 + i, False, scores, alpha, beta, h)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = float('inf')
        for i in range(2):
            val = alphabeta(depth + 1, nodeIndex * 2 + i, True, scores, alpha, beta, h)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

scores = [3, 5, 6, 9, 1, 2, 0, -1]
h = 3
print("Optimal value with Alpha-Beta Pruning:", alphabeta(0, 0, True, scores, float('-inf'), float('inf'), h))