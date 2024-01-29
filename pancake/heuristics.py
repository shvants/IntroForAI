def base_heuristic(pancake_state):
    state_str = pancake_state.get_state_str()
    pancakes = list(map(int, state_str.split(',')))
    total_pancakes = len(pancakes)
    heuristic_value = 0

    for i in range(total_pancakes):
        current_pancake = pancakes[i]
        if current_pancake != total_pancakes - i:
            heuristic_value = sum(pancakes[i:])
            break

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