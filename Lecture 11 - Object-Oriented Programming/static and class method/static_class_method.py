from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass
    
    @staticmethod
    def shape_info():
        """Static method to provide general information about shapes."""
        print("Shapes are geometric figures with different properties.")

    @classmethod
    def number_of_sides(cls):
        """Class method to provide general information about the number of sides."""
        raise NotImplementedError("Subclasses must implement this method.")

# Concrete class for Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        """Override the abstract method to calculate area of a circle."""
        return 3.14159 * (self.radius ** 2)
    
    @classmethod
    def number_of_sides(cls):
        """Override the class method to provide information specific to circles."""
        return 0  # A circle has no sides

# Concrete class for Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        """Override the abstract method to calculate area of a rectangle."""
        return self.width * self.height
    
    @classmethod
    def number_of_sides(cls):
        """Override the class method to provide information specific to rectangles."""
        return 4  # A rectangle has 4 sides

# Usage of static and class methods
Shape.shape_info()  # Output: Shapes are geometric figures with different properties.

print("Circle sides:", Circle.number_of_sides())  # Output: Circle sides: 0
print("Rectangle sides:", Rectangle.number_of_sides())  # Output: Rectangle sides: 4

# Creating instances of shapes and calculating areas
circle = Circle(radius=5)
rectangle = Rectangle(width=4, height=6)

print("Circle area:", circle.area())  # Output: Circle area: 78.53975
print("Rectangle area:", rectangle.area())  # Output: Rectangle area: 24
