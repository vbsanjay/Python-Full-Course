# A test class where I experiment
class Rectangle:
    def __init__(self, length, width):
        self.height = length;
        self.width = width;

    # _width and _height are attributes
    # width and height are properties that control access to these attributes

    # Getter
    @property
    def width(self):
        return self._width
    
    @property
    def height(self):
        return self._height

    #Setter 
    @width.setter
    def width(self, width):
        if width < 0:
            raise ValueError("Width must be positive")
        else:
            self._width = width
    
    @height.setter
    def height(self, height):
        if height < 0:
            raise ValueError("height must be positive")
        else:
            self._height = height

    def field_printer(self):
        print(self._height)
        print(self._width)
    
    def find_area(self):
        return self.height * self.width

    def find_perimeter(self):
        return 2 * (self.height + self.width)
    
    def __str__(self): # readable output for end user
        return 'rectangle of length={0} width={1}'.format(self.height, self.width)

    def __eq__(self, other):
        if isinstance(other, Rectangle): #if tried to compare rectangle type with any other type
            return False
        if self.height == other.length and self.width == other.width:
            return True
        return False

    def __repr__(self): # official development output for developers to debug
        return 'Rectangle ({0},{1})'.format(self.height, self.width)
    
    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.find_area() < other.find_area()
        else:
            return False
    

rectangle = Rectangle(10, 4)
# area = rectangle.find_area()
# print(area)
print(rectangle)
print(repr(rectangle))
rectangle.width= 10
print(rectangle.width)
rectangle.height = 40
print(rectangle.height)

rectangle_2 = Rectangle(20,4)
print(rectangle == rectangle_2)
print(rectangle < rectangle_2)
# we haven't implemented greater than in code however 
# python figures it out itself form __lt__ function we implemented
print(rectangle_2 > rectangle) 
print(vars(rectangle_2))