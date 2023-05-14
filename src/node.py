class Node:
    RADIUS = 12
    DISPLAY_OPTIONS = {'outline': 'black', 'fill': '#ccff99'}

    def __init__(self, num, x, y):
        self.num = num
        self.x = x
        self.y = y

    def contains_point(self, x, y):
        if (x - self.x)**2 + (y - self.y)**2 <= self.RADIUS * self.RADIUS:
            return True
        return False
