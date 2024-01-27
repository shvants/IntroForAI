def base_heuristic(_pancake_state):
    # Get the state string from the _pancake_state object
    state_str = _pancake_state.state_str
    heuristic_value = 0

    # Split the state string into a list of pancakes
    pancakes = state_str.split(',')

    # Iterate through the pancakes from top to bottom
    for i in range(len(pancakes)):
        # Check if the pancake is not in its correct position
        if int(pancakes[i]) != i + 1:
            # Add the value of the pancake to the heuristic
            heuristic_value += int(pancakes[i])
            # print(heuristic_value)

    return heuristic_value

def advanced_heuristic(_pancake_state):
    state_str = _pancake_state.state_str
    pancakes = [int(p) for p in state_str.split(',')]
    gap_count = 0

    # Iterate through the pancakes and count the gaps
    for i in range(len(pancakes) - 1):
        if abs(pancakes[i] - pancakes[i + 1]) != 1:
            gap_count += 1

    return gap_count