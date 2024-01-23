from search_node import search_node
import heapq

open_hash = {}


def create_open_set():
    return []


def create_closed_set():
    return {}


def add_to_open(vn, open_set, open_hash):
    if open_hash.get(vn.state) is None:
        heapq.heappush(open_set, vn)
        open_hash[vn.state] = vn
    else:
        existing_node = open_hash[vn.state]
        existing_node.update_node(vn)


def open_not_empty(open_set):
    if open_set:
        return True
    return False


def get_best(open_set):
    best = heapq.heappop(open_set)
    open_hash.pop(best.state)
    return best


def add_to_closed(vn, closed_set):
    pass


# returns False if curr_neighbor state not in open_set or has a lower g from the node in open_set
# remove the node with the higher g from open_set (if exists)
def duplicate_in_open(vn, open_set):
    if open_hash.get(vn.state) is None:
        return False
    elif open_hash.get(vn.state).g > vn.g:



    else:
        return True


# returns False if curr_neighbor state not in closed_set or has a lower g from the node in closed_set
# remove the node with the higher g from closed_set (if exists)
def duplicate_in_closed(vn, closed_set):
    pass


def print_path(path):
    for i in range(len(path) - 1):
        print(f"[{path[i].state.get_state_str()}]", end=", ")
    print(path[-1].state.state_str)


def search(start_state, heuristic, goal_state):
    open_set = create_open_set()  # minimum heap
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
