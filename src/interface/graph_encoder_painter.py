from tkinter import *
from .node import Node
from .graph_encoder import GraphEncoder

class GraphEncoderPainter:
    def __init__(self):
        self.root = Tk()
        self.nodes = []
        self.v_neighbours = []
        self.start_node = None

    def perform(self):
        self.initialize_canvas()

    def initialize_canvas(self):
        self.root.title("Insert graph")
        self.root.geometry('800x600')

        self.canvas = Canvas(self.root, width=800, height=600, bg='white')
        self.canvas.pack()

        self.canvas.create_rectangle(750, 550, 800, 600, fill='green')
        self.canvas.create_line(760, 570, 770, 590, fill='white', width=4)
        self.canvas.create_line(769, 590, 790, 560, fill='white', width=4)
        

        self.root.bind("<Button-1>", self.create_node)
        self.root.bind("<Button-2>", self.connect_nodes)
        self.root.mainloop()

    def create_node(self, event):
        x = int(event.x) 
        y = int(event.y)

        if (x >= 750 and y >= 550):
            print('Введенные вершины:')
            print(self.v_neighbours)

            encoder = GraphEncoder(self.v_neighbours)
            code = list(map(str, encoder.encode()))

            self.canvas.delete('all')
            self.canvas.create_text(200, 200, text=f"The code is: {' '.join(code)}", fill='black', font=('Helvetica 15 bold'))
            return code
        
        node_id = len(self.nodes)
        self.canvas.create_oval(x - Node.RADIUS, y - Node.RADIUS,
                                x + Node.RADIUS, y + Node.RADIUS,
                                Node.DISPLAY_OPTIONS)
        self.canvas.create_text(x, y, text=str(node_id + 1), fill='black', font=('Helvetica 15 bold'))

        self.v_neighbours.append([])
        self.nodes.append(Node(node_id, x, y))

    def connect_nodes(self, event):
        x = int(event.x) 
        y = int(event.y)

        for node in self.nodes:
            if node.contains_point(x, y):
                if self.start_node is None:
                    self.start_node = node
                else:
                    self.v_neighbours[self.start_node.num].append(node.num) # для каждой вершины храним ее соседей
                    self.v_neighbours[node.num].append(self.start_node.num)

                    line = self.canvas.create_line(self.start_node.x, self.start_node.y,
                                            node.x, node.y, fill='green', width=5)
                    self.canvas.tag_lower(line)
                    self.start_node = None

        return self.v_neighbours
        