import itertools

def solve_cryptarithmetic():
    # Unique letters in the puzzle
    letters = 'SENDMORY'  # All distinct letters in SEND + MORE = MONEY
    digits = range(10)

    # Generate all possible permutations of digits for the letters
    for perm in itertools.permutations(digits, len(letters)):
        letter_map = dict(zip(letters, perm))

        # Skip if M or S is 0 (no leading zeroes)
        if letter_map['M'] == 0 or letter_map['S'] == 0:
            continue

        # Form numbers based on the mapping
        send = 1000 * letter_map['S'] + 100 * letter_map['E'] + 10 * letter_map['N'] + letter_map['D']
        more = 1000 * letter_map['M'] + 100 * letter_map['O'] + 10 * letter_map['R'] + letter_map['E']
        money = 10000 * letter_map['M'] + 1000 * letter_map['O'] + 100 * letter_map['N'] + 10 * letter_map['E'] + letter_map['Y']

        if send + more == money:
            print(f"SEND + MORE = MONEY")
            print(f"{send} + {more} = {money}")
            print("Letter Mapping:", letter_map)
            return

    print("No solution found.")

# Run the solver
solve_cryptarithmetic()
