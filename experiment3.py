from collections import deque

def water_jug_bfs(jug1_capacity, jug2_capacity, target):
    visited = set()
    queue = deque()
    steps = []

    # Initial state (0, 0)
    queue.append((0, 0))
    visited.add((0, 0))

    while queue:
        jug1, jug2 = queue.popleft()
        steps.append((jug1, jug2))

        if jug1 == target or jug2 == target:
            print("Steps to reach the target:")
            for step in steps:
                print(step)
            return True

        # All possible next states
        possible_states = [
            (jug1_capacity, jug2),        # Fill jug1
            (jug1, jug2_capacity),        # Fill jug2
            (0, jug2),                    # Empty jug1
            (jug1, 0),                    # Empty jug2
            (jug1 - min(jug1, jug2_capacity - jug2), jug2 + min(jug1, jug2_capacity - jug2)),  # Pour jug1 -> jug2
            (jug1 + min(jug2, jug1_capacity - jug1), jug2 - min(jug2, jug1_capacity - jug1))   # Pour jug2 -> jug1
        ]

        for state in possible_states:
            if state not in visited:
                visited.add(state)
                queue.append(state)

    print("No solution found.")
    return False

# Example usage
water_jug_bfs(4, 3, 2)
