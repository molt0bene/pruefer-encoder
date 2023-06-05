import pygraphviz as PG
from graphviz import Source

class GraphDecoder:
    def __init__(self, code):
        self.code = [*map(lambda x: x - 1, code)]

    def perform(self):
        self.build_graph()

    def encode(self):
        n = len(self.code) + 2  # Number of vertices
        degree = [1] * n  # Degree of each vertex, initialize to 1

        for v in self.code:
            degree[v] += 1
        tree_edges = []

        for i in range(n - 2):
            # Find the smallest numbered leaf
            leaf = min(v for v in range(n) if degree[v] == 1)
            # Find its neighbor using the Prüfer code
            neighbor = self.code[i]
            # Add the edge to the tree and update degrees
            tree_edges.append((leaf, neighbor))
            degree[leaf] -= 1
            degree[neighbor] -= 1

        # The last two vertices are connected by an edge
        last_two = [v for v in range(1, n) if degree[v] == 1]
        tree_edges.append((last_two[0], last_two[1]))

        return tree_edges
    
    def build_graph(self):
        A = PG.AGraph(directed=False, strict=True)
        tree_edges = self.encode()

        for edge in tree_edges:
            A.add_edge(edge[0] + 1, edge[1] + 1)

        A.write('ademo.dot')
        A.layout(prog='dot')
        s = Source.from_file('ademo.dot')
        s.view()
