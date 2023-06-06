from .node import Node

class GraphEncoder:
    def __init__(self, v_neighbours):
        self.v_neighbours = v_neighbours

    def check_tree(self):
        for vertex in self.v_neighbours:
            if vertex == []:
                return False
            
        return True

    def encode(self):
        if not self.check_tree():
            return ["Error", "All vertices must be connected."]
        n = len(self.v_neighbours)
        pruefer_code = []
        degree = [len(self.v_neighbours[i]) for i in range(n)]
        
        try:
            for i in range(n-2):
                # Находим лист с минимальным номером
                leaf = min([j for j in range(n) if degree[j] == 1])
                
                # Находим ее соседа и добавляем к коду
                neighbor = self.v_neighbours[leaf][0]
                pruefer_code.append(neighbor + 1)
                
                # Удаляем лист из дерева
                degree[leaf] = 0
                degree[neighbor] -= 1
                self.v_neighbours[neighbor].remove(leaf)
        except:
            return ["Error", "Either the graph is not a tree or data is incorrect."]
        
        return ["Success", pruefer_code]
