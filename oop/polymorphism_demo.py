import math

class Shape:
    
    def area(self):
        raise NotImplementedError()
    
    
    
class  Rectangle(Shape):
    def __init__(self, width, length):
        self.length=length
        self.width=width
        
        
    def area(self):
        return super().area() + self.width * self.length
    
    
    
class Circle(Shape):
    
    def __init__(self,radius) -> None:
        self.radius=radius
        
    def area(self):
        return super().area() + math.pi * (self.radius ** 2)

        
    