from tkinter import *
from node import Node

class GraphEncoder:
    def __init__(self):
        self.root = Tk()
        self.nodes = []
        self.vertices = []
        self.start_node = None

    def perform(self):
        self.initialize_canvas()

    def initialize_canvas(self):
        self.root.title("Insert graph")
        self.root.geometry('800x600')

        self.canvas = Canvas(self.root, width=800, height=600, bg='white')
        self.canvas.pack()

        self.root.bind("<Button-1>", self.create_node)
        self.root.bind("<Button-2>", self.connect_nodes)
        self.root.mainloop()

    def create_node(self, event):
        x = int(event.x) 
        y = int(event.y)

        self.canvas.create_oval(x - Node.RADIUS, y - Node.RADIUS,
                                x + Node.RADIUS, y + Node.RADIUS,
                                Node.DISPLAY_OPTIONS)
        self.canvas.create_text(x, y, text=str(len(self.nodes)), fill='black', font=('Helvetica 15 bold'))

        self.nodes.append(Node(id, x, y))

    def connect_nodes(self, event):
        x = int(event.x) 
        y = int(event.y)

        for node in self.nodes:
            if node.contains_point(x, y):
                if self.start_node is None:
                    self.start_node = node
                else:
                    self.vertices.append([self.start_node.num, node.num])
                    line = self.canvas.create_line(self.start_node.x, self.start_node.y,
                                            node.x, node.y, fill='green', width=5)
                    self.canvas.tag_lower(line)
                    self.start_node = None

        return self.vertices
