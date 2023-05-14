from tkinter import *

class GraphEncoder:
    def perform(self):
        self.initialize_canvas()

    def initialize_canvas(self):
        root = Tk()
        root.title("Insert graph")
        root.geometry('800x600')

        root.bind("<Button-1>", self.leftclick)
        root.mainloop()

    def leftclick(self, event):
        print('kajfafj:', str(event.x) + "," + str(event.y))
