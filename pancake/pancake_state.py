class pancake_state:

    def __init__(self, state_str):
        self.state_str = state_str
        #you may add data stractures to improve the search




    #returns an array of tuples of neighbor states and the cost to reach them: [(pancake_state1, cost1), (pancake _state2, cost2)...]
    # def get_neighbors(self):
    #     neighbors = []
    #     pancakes = list(map(int, self.state_str.split(',')))
    #     n = len(pancakes)
    #
    #     # Flip starting from the third-to-last index to the first index
    #     for i in range(n - 2, 0, -1):
    #         flipped_end = pancakes[:i] + pancakes[i:][::-1]
    #         neighbor_state = ','.join(map(str, flipped_end))
    #         cost = self.flip_cost(pancakes[i:])
    #         neighbors.append((pancake_state(neighbor_state), cost))
    #
    #     # Additionally, handle flipping the entire stack
    #     flipped_entire = pancakes[::-1]
    #     neighbor_entire = ','.join(map(str, flipped_entire))
    #     cost_entire = self.flip_cost(flipped_entire)
    #     neighbors.append((pancake_state(neighbor_entire), cost_entire))
    #
    #     return neighbors

    def get_neighbors(self):
        neighbors = []
        pancakes = list(map(int, self.state_str.split(',')))
        n = len(pancakes)

        # Loop starting from flipping the entire stack to no flip
        for i in range(n - 2,-1,-1):
            flipped_end = pancakes[:i] + pancakes[i:][::-1]
            neighbor_state = ','.join(map(str, flipped_end))
            cost = self.flip_cost(pancakes[i:])
            neighbors.append((pancake_state(neighbor_state), cost))

        return neighbors
    def flip_cost(self, pancakes_to_flip):
        return sum(pancakes_to_flip)

    #you can change the body of the function if you want

    def __hash__(self):
        return hash(self.state_str)

    #you can change the body of the function if you want
    def __eq__(self, other):
        return self.state_str == other.state_str


    def get_state_str(self):
        return self.state_str
