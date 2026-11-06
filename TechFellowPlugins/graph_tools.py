def breadth_first_search(graph, start):
    """Visit graph nodes level by level."""

    visited = []
    queue = [start]
    while queue:
        current_node = queue.pop(0)
        if current_node not in visited:
            visited.append(current_node)
            for i in graph.get(current_node, []):
                if i not in visited:
                    queue.append(i)
    return visited

def depth_first_search(graph, start):
    """Visit graph nodes by exploring each branch deeply."""
    visited = []
    queue = [start]
    while queue:
        current_node = queue.pop()
        if current_node not in visited:
            visited.append(current_node)
            for i in graph.get(current_node, []):
                if i not in visited:
                    queue.append(i)
    return visited

def find_shortest_path(graph, start, end):
    """Find the shortest path between two nodes using BFS."""
    if start==end:
        return [start]
    
    queue = [[start]]
    visited = set()

    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node == end:
            return path
        if node not in visited:
            visited.add(node)
            for i in graph.get(node, []):
                if i not in visited:
                    queue.append(path + [i])

    return None


def is_graph_connected(graph):
    """Check whether all graph nodes are reachable from the first node."""

    start = next(iter(graph))
    visited = breadth_first_search(graph, start)

    all_nodes = set(graph)

    for neighbours in graph.values():
        all_nodes.update(neighbours)

    for node in all_nodes:
        if node not in visited:
            return False
    return True


def find_connected_components(graph):
    """Find separate connected groups in an undirected graph."""
    all_nodes = set(graph)

    for neighbours in graph.values():
        all_nodes.update(neighbours)

    visited = set()
    components = []

    for node in all_nodes:
        if node not in visited:
            component = breadth_first_search(graph, node)
            visited.update(component)
            components.append(component)

    return components