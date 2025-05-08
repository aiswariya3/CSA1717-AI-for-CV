def vacuum_cleaner_problem(state):
    """
    State is a tuple: (vacuum_location, room_A_status, room_B_status)
    vacuum_location: 'A' or 'B'
    room_A_status, room_B_status: 'Clean' or 'Dirty'
    """
    actions = []

    location, A_status, B_status = state

    if location == 'A':
        if A_status == 'Dirty':
            actions.append('Suck')
            A_status = 'Clean'
        if B_status == 'Dirty':
            actions.append('Move Right')
            location = 'B'
            actions.append('Suck')
            B_status = 'Clean'
    elif location == 'B':
        if B_status == 'Dirty':
            actions.append('Suck')
            B_status = 'Clean'
        if A_status == 'Dirty':
            actions.append('Move Left')
            location = 'A'
            actions.append('Suck')
            A_status = 'Clean'

    print("Final room statuses: A =", A_status, ", B =", B_status)
    return actions

# Example usage:
initial_state = ('A', 'Dirty', 'Dirty')
actions_taken = vacuum_cleaner_problem(initial_state)
print("Actions taken:", actions_taken)
