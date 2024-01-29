class pancake_state:

    def __init__(self, state_str):
        self.state_str = state_str
        #you may add data stractures to improve the search

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
