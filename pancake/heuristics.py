def base_heuristic(_pancake_state):
    state_str = _pancake_state.get_state_str()
    pancakes = list(map(int, state_str.split(',')))
    total_pancakes = len(pancakes)
    heuristic_value = 0

    for i in range(total_pancakes):
        current_pancake = pancakes[i]
        if current_pancake != total_pancakes - i:
            heuristic_value = sum(pancakes[i:])
            break

    return heuristic_value

cache = {1: 1, 2: 3, 3: 6, 4: 10, 5: 15, 6: 21, 7: 28, 8: 36, 9: 45}

def advanced_heuristic(_pancake_state):
    state_str = _pancake_state.get_state_str()
    pancakes = tuple(map(int, state_str.split(',')))
    total_pancakes = len(pancakes)
    heuristic_value = 0

    for i in range(total_pancakes):
        current_pancake = pancakes[i]
        if current_pancake != total_pancakes - i:
            heuristic_value = cache[total_pancakes - i]
            break

    return heuristic_value

# def advanced_heuristic(_pancake_state):
#     pancakes = tuple(map(int, _pancake_state.state_str.split(',')))
#     gap_count = 0
#     pancake_count = len(pancakes)
#     if pancake_count[0] != pancake_count - 1:
#         gap_count += 1
#     for i in range(pancake_count - 1):
#         if abs(pancakes[i] - pancakes[i + 1] != 1):
#             gap_count += 1
#
#     return gap_count



# def advanced_heuristic(_pancake_state):
#     # Convert the state to a string key for caching
#     state_str = _pancake_state.get_state_str()
#
#     # Check if the heuristic value for this state is already in the cache
#     if state_str in cache:
#         return cache[state_str]
#
#     # Compute the heuristic value if not in the cache
#     pancakes = tuple(map(int, state_str.split(',')))
#     gap_count = 0
#     pancake_count = len(pancakes)
#     for i in range(pancake_count - 1):
#         if abs(pancakes[i] - pancakes[i + 1]) != 1:
#             gap_count += 1
#
#     # Store the computed value in the cache
#     cache[state_str] = gap_count
#
#     return gap_count
