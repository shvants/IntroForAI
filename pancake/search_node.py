class search_node():
    def __init__(self, state, g=0, h=0, prev=None):
        self.state = state
        self.g = g
        self.h = h
        self.f = g + h
        self.prev = prev

    def __lt__(self, other):
        return (self.f < other.f) or (self.f == other.f and self.h < other.h)

    def get_neighbors(self):
        return self.state.get_neighbors()


    def update_node(existing_node, new_node):
        """
        Updates the existing search_node with the values from the new search_node.

        :param existing_node: The search_node to be updated.
        :param new_node: The search_node with the new values.
        """
        existing_node.g = new_node.g
        existing_node.h = new_node.h
        existing_node.f = new_node.f
        existing_node.prev = new_node.prev
