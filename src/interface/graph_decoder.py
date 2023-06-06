import pygraphviz as PG
from graphviz import Source

class GraphDecoder:
    def __init__(self, code):
        self.code = [*map(lambda x: x - 1, code)]

    def perform(self):
        self.build_graph()

    def decode(self):
        n = len(self.code) + 2  # Число вершин
        degree = [1] * n  # Степень каждой вершины, изначально 1

        for v in self.code:
            degree[v] += 1
        tree_edges = []

        for i in range(n - 2):
            # Находим лист с минимальным номером
            leaf = min(v for v in range(n) if degree[v] == 1)
            # Находим его соседа по коду Прюфера
            neighbor = self.code[i]
            # Добавляем ребро и обновляем степени
            tree_edges.append((leaf, neighbor))
            degree[leaf] -= 1
            degree[neighbor] -= 1

        # Добавляем ребро последних двух вершин
        last_two = [v for v in range(1, n) if degree[v] == 1]
        tree_edges.append((last_two[0], last_two[1]))

        return tree_edges
    
    def build_graph(self):
        A = PG.AGraph(directed=False, strict=True)
        tree_edges = self.decode()

        for edge in tree_edges:
            A.add_edge(edge[0] + 1, edge[1] + 1)

        A.write('ademo.dot')
        A.layout(prog='dot')
        s = Source.from_file('ademo.dot')
        s.view()
