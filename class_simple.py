class Rectangle(object):
    """simple example of a class that defines the width and height of a 
    rectangle
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height


r = Rectangle(10, 14)

print("Width: {:d}".format(r.width))

# Notes
# - To make a protected member, add "_" as a prefix. Example: self._width