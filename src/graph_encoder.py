from tkinter import *
from node import Node

class GraphEncoder:
    def __init__(self):
        self.root = Tk()
        self.nodes = []

    def perform(self):
        self.initialize_canvas()

    def initialize_canvas(self):
        self.root.title("Insert graph")
        self.root.geometry('800x600')

        self.canvas = Canvas(self.root, width=800, height=600, bg='white')
        self.canvas.pack()

        self.root.bind("<Button-1>", self.create_node)
        self.root.mainloop()

    def create_node(self, event):
        x = int(event.x) 
        y = int(event.y)

        self.canvas.create_oval(x - Node.RADIUS, y - Node.RADIUS,
                                x + Node.RADIUS, y + Node.RADIUS,
                                Node.DISPLAY_OPTIONS)

