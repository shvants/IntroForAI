class pancake_state:

    def __init__(self, state_str):
        self.state_str = state_str
        # you may add data structures to improve the search

    # returns an array of tuples of neighbor states and the cost to reach them: [(pancake_state1, cost1),
    # (pancake _state2, cost2)...]
    """
    :param self 
    :returns list of tuples containing state and cost for each of the neighbors of the current state
    """
    def get_neighbors(self):
        pass

    # you can change the body of the function if you want
    def __hash__(self):
        return hash(self.state_str)

    # you can change the body of the function if you want
    def __eq__(self, other):
        return self.state_str == other.state_str

    def get_state_str(self):
        return self.state_str



    """ 
    :param state as a string  
    :return value of cost as integer ?  or string 
    """
    def calc_cost_state(self, pancake_str):
        return

    """
    :param index as str/int
    :param pancake state as str
    :return flipped pancake state as str
    """
    def flip(self, pancake_str, index):
        return
