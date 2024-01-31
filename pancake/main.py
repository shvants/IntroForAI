import random

from search import search
from pancake_state import pancake_state
from heuristics import *
import timeit

# if __name__ == '__main__':
#     goal_state = "4,3,2,1"
#     pancake_input = "4,2,3,1"
#     pancake_state = pancake_state(pancake_input)
#     search_result = search(pancake_state, base_heuristic, goal_state)
#     search_result2 = search(pancake_state, advanced_heuristic, goal_state)




if __name__ == '__main__':
    goal_state = "9,8,7,6,5,4,3,2,1"

    for _ in range(10):
        # Generate a random pancake input
        pancake_input = ','.join(map(str, random.sample(range(1, 10), 9)))
        print(f"Pancake Input: {pancake_input}")

        pancake_state_instance = pancake_state(pancake_input)

        # Measure execution time for base heuristic search
        start_time_base = timeit.default_timer()
        search_result = search(pancake_state_instance, base_heuristic, goal_state)
        end_time_base = timeit.default_timer()
        print("Base Heuristic Search Time:", end_time_base - start_time_base)

        # Print base heuristic search results g values
        for i in search_result:
            print("Base g value:", i.g)
            print("Base h value:", i.h)


        # Measure execution time for advanced heuristic search
        start_time_adv = timeit.default_timer()
        search_resultAdv = search(pancake_state_instance, advanced_heuristic, goal_state)
        end_time_adv = timeit.default_timer()
        print("Advanced Heuristic Search Time:", end_time_adv - start_time_adv)

        # Print advanced heuristic search results g values
        for i in search_resultAdv:
            print("Advanced g value:", i.g)
            print("Advanced h value:", i.h)

        print("----------")
