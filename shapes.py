import numpy as np

class Shape:
    name = "Generic"
    def __init__(self):
        pass

    def get_area(self):
        # raise NotImplementedError
        return float(-1)

    def get_perimeter(self):
        # raise NotImplementedError
        return float(-1)

class Circle(Shape):
    name = "Circle"
    def __init__(self,r):
        self.r = float(r)

    def get_area(self):
        return np.pi * self.r**2

    def get_perimeter(self):
        return 2 * np.pi * self.r

class Rectangle(Shape):
    name = "Rectangle"
    def __init__(self,l,w):
        self.l = float(l)
        self.w = float(w)

    def get_area(self):
        return self.l * self.w

    def get_perimeter(self):
        return 2*self.l + 2*self.w

class Square(Rectangle):
    name = "Square"
    def __init__(self,l):
        super().__init__(l=l,w=l)
        
class UnitSquare(Square):
    name = "1-Square"
    def __init__(self):
        super().__init__(l=1)

def print_shape_info(sh):
    print(f"Shape: {sh.name : >10}\tArea: {sh.get_area():>02.2f}\tPeri: {sh.get_perimeter():>02.2f}")
    
def example_run():
    sha = Shape()
    circ = Circle(1)
    rect = Rectangle(2,3)
    rect_s = Rectangle(5,5)
    sq = Square(5)

    shapes = [sha,circ,rect,rect_s,sq]

    for sha in shapes:
        print_shape_info(sha)
    # Done

if __name__ == "__main__":
    example_run()