class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move_right(self):
        self.x += 1

    def move_left(self):
        self.x -= 1

    def move_up(self):
        self.y += 1

    def move_down(self):
        self.y -= 1

    # (3, 5)
    def __repr__(self):
        return f"({self.x}, {self.y})"
