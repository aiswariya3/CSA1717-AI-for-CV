from collections import deque
start = "123405678"  
goal = "123456780"    
queue = deque()
queue.append((start, []))
visited = set()

while queue:
    state, path = queue.popleft()
    if state == goal:
        path.append(state)
        for step in path:
            for i in range(0, 9, 3):
                print(step[i:i+3])
            print()
        break
    visited.add(state)
    i = state.index('0')
    x, y = divmod(i, 3)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            ni = nx * 3 + ny
            lst = list(state)
            lst[i], lst[ni] = lst[ni], lst[i]
            new_state = ''.join(lst)
            if new_state not in visited:
                queue.append((new_state, path + [state]))
