#1ex
from typing import Self
class InputString :
    Self.input_string = ""
def getstring(self):    
    self.input_string = input("Enter: ")
def printstring (self):
    print(self.input_string.upper())
    
    #2ex
class shape :
    def area(self):
        return 0;
class square(shape):
    def __init__(self, length):
        self.length = length
    def srea (self):
        return self.length **2
    
    #ex3
class rectangle(shape) :
    def __init__ (self, length, width ):
        self.lenght = length
        self.width = width
    def area(self):
        return self.length * self.width
    
    #ex4
    class point :
        def __init__ (self, x, y):
            self.x = x
            self.y = y
        def show(self):
            print(f"coordinates: ({self.x}, {self.y})")
        def move(self, x1, y1):
            self.x1=x1
            self.y1=y1 
        def dist (self, point_1):
            return((self.x - point_1.x)**2 + (self.y - point_1.y)**2)**0,5
        
        
        
        