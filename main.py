dfs_visit_order = []
bfs_visit_order = []


class GraphNode:
    def __init__(self, name, neighbors):
        self.name = name
        self.neighbors = neighbors
        self.visited = 0

    def mark_as_visited(self):
        self.visited = 1

    def traverse_dfs(self):
        if self.visited:
            return
        dfs_visit_order.append(self.name)
        self.mark_as_visited()
        for neighbor_name in self.neighbors:
            graph_nodes[neighbor_name].traverse_dfs()

    def traverse_bfs(self):
        queue = [self]
        while queue:
            current = queue.pop(0)
            if current.visited:
                continue
            bfs_visit_order.append(current.name)
            current.mark_as_visited()
            for neighbor_name in current.neighbors:
                candidate = graph_nodes[neighbor_name]
                if not candidate.visited:
                    queue.append(candidate)


graph_nodes = {
    'A': GraphNode('A', ['B', 'C', 'D']),
    'B': GraphNode('B', ['A', 'E', 'F']),
    'C': GraphNode('C', ['A', 'F', 'G']),
    'D': GraphNode('D', ['A', 'G', 'H', 'I']),
    'E': GraphNode('E', ['B', 'J']),
    'F': GraphNode('F', ['B', 'C', 'E']),
    'G': GraphNode('G', ['C', 'D']),
    'H': GraphNode('H', ['D']),
    'I': GraphNode('I', ['D']),
    'J': GraphNode('J', ['E', 'F']),
}

def reset_graph_state():
    global dfs_visit_order, bfs_visit_order
    dfs_visit_order = []
    bfs_visit_order = []
    for node in graph_nodes.values():
        node.visited = False

reset_graph_state()
graph_nodes['A'].traverse_dfs()
print(*dfs_visit_order)

reset_graph_state()
graph_nodes['A'].traverse_bfs()
print(*bfs_visit_order)