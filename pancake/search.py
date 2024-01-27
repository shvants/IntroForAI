from search_node import search_node
import heapq

def create_open_set():
    return [], {} #creating them as a tuple of (heap,dictionary (hashtable))


def create_closed_set():
    return set()


def add_to_open(node, open_set):
    heap, dictionary = open_set
    state_str = node.state.get_state_str()
    if state_str in dictionary:
        if dictionary[state_str].g > node.g:
            # Update existing node's values
            dictionary[state_str].update_node(node)
        return
    heapq.heappush(heap, node)
    dictionary[state_str] = node



def open_not_empty(open_set):
    heap, _ = open_set
    return len(heap) > 0


def get_best(open_set):
    heap, dictionary = open_set
    while heap:
        node = heapq.heappop(heap)
        state_str = node.state.get_state_str()
        if dictionary.get(state_str) is node:
            return node
    return None

def add_to_closed(node, closed_set):
    closed_set.add(node.state.get_state_str())



# returns False if curr_neighbor state not in open_set or has a lower g from the node in open_set
# remove the node with the higher g from open_set (if exists)
def duplicate_in_open(node, open_set):
    hp, dictionary = open_set
    state_str = node.state.get_state_str()
    if state_str in dictionary and dictionary[state_str].g <= node.g:
        return True
    #updatenode happens in the add
    return False

# returns False if curr_neighbor state not in closed_set or has a lower g from the node in closed_set
# remove the node with the higher g from closed_set (if exists)
def duplicate_in_closed(node, closed_set):
    state_str = node.state.get_state_str()
    if state_str in closed_set:
        return True
    return False


def print_path(path):
    for i in range(len(path) - 1):
        print(f"[{path[i].state.get_state_str()}]", end=", ")
    print(path[-1].state.state_str)


def search(start_state, heuristic, goal_state):
    open_set = create_open_set()
    closed_set = create_closed_set()
    start_node = search_node(start_state, 0, heuristic(start_state))
    add_to_open(start_node, open_set)

    while open_not_empty(open_set):

        current = get_best(open_set)

        if current.state.get_state_str() == goal_state:
            path = []
            while current:
                path.append(current)
                current = current.prev
            path.reverse()
            return path

        add_to_closed(current, closed_set)

        for neighbor, edge_cost in current.get_neighbors():
            curr_neighbor = search_node(neighbor, current.g + edge_cost, heuristic(neighbor), current)
            if not duplicate_in_open(curr_neighbor, open_set) and not duplicate_in_closed(curr_neighbor, closed_set):
                add_to_open(curr_neighbor, open_set)

    return None

