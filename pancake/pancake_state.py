class pancake_state:

    def __init__(self, state_str):
        self.state_str = state_str
        #you may add data stractures to improve the search


    #returns an array of tuples of neighbor states and the cost to reach them: [(pancake_state1, cost1), (pancake _state2, cost2)...]
    def get_neighbors(self):
        neighbors = []
        pancakes = self.state_str.split(',')
        n = len(pancakes)

        for i in range(2, n + 1):
            flipped = pancakes[:i][::-1] + pancakes[i:]
            neighbor_state = ','.join(flipped)
            cost = self.flip_cost(pancakes[:i])
            neighbors.append((pancake_state(neighbor_state), cost))

        return neighbors

    def flip_cost(self, pancakes_to_flip):
        # Cost is the sum of the numbers of the pancakes being flipped
        return sum(map(int, pancakes_to_flip))

    #you can change the body of the function if you want

    def __hash__(self):
        return hash(self.state_str)

    #you can change the body of the function if you want
    def __eq__(self, other):
        return self.state_str == other.state_str


    def get_state_str(self):
        return self.state_str
