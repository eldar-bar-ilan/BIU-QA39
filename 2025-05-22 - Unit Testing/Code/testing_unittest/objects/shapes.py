class Rectangle:
    # constructor method - creates the object
    def __init__(self, height=0, width=0):
        if height >= 0 and width >= 0:
            self.height = height
            self.width = width
        else:
            self.height = 0
            self.width = 0

    # returns a string representation of the object
    def __repr__(self):
        return f"[Rectangle {self.height} X {self.width}]"

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)

    def resize(self, height, width):
        if height >= 0 and width >= 0:
            self.height = height
            self.width = width
            return True
        else:
            return False

    # url = www....../retangle/paint?h=?andw=?
    def paint(self):
        print("paint the rectangle in HTML for users to see")

if __name__ == "__main__":
    r1 = Rectangle()
    r2 = Rectangle(55, 76)
    print(r1)
    print(r2)

    r1.resize(-9, -6)
    print(r1)
