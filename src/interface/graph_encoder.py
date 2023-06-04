from .node import Node

class GraphEncoder:
    def __init__(self, v_neighbours):
        self.v_neighbours = v_neighbours

    def encode(self):
        n = len(self.v_neighbours)
        pruefer_code = []
        degree = [len(self.v_neighbours[i]) for i in range(n)]
        
        # Encode the tree using Prüfer's algorithm
        for i in range(n-2):
            # Find leaf node with smallest label
            leaf = min([j for j in range(n) if degree[j] == 1])
            
            # Find its neighbor and add it to the code
            neighbor = self.v_neighbours[leaf][0]
            pruefer_code.append(neighbor)
            
            # Remove the leaf from the tree
            degree[leaf] = 0
            degree[neighbor] -= 1
            self.v_neighbours[neighbor].remove(leaf)
        
        print(*pruefer_code)
        return pruefer_code
