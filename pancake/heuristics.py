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

# cache = {1: 1, 2: 3, 3: 6, 4: 10, 5: 15, 6: 21, 7: 28, 8: 36, 9: 45}

# def advanced_heuristic(_pancake_state):
#         state_str = _pancake_state.get_state_str()
#         pancakes = state_str.split(',')  # No need to convert to tuple
#
#         total_pancakes = len(pancakes)
#
#         for i in range(total_pancakes):
#             if int(pancakes[i]) != total_pancakes - i:
#                 return cache[total_pancakes - i]
#
#         return 0

def advanced_heuristic(_pancake_state):
    state_str = _pancake_state.get_state_str()
    pancakes = tuple(map(int, state_str.split(',')))
    gap_cost = 0

    for i in range(len(pancakes) - 1):
        # Calculate gap cost
        if abs(pancakes[i] - pancakes[i + 1]) != 1:
            #normalizing the gap differences
            gap_cost += 0.5*(pancakes[i] + pancakes[i + 1])

        #if the pancake is not in its correct place, we will add its value because we will have to flip it in the future
        correct_value = len(pancakes) - i
        if pancakes[i] != correct_value:
            gap_cost += pancakes[i]

    return gap_cost