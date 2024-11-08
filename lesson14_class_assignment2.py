'''
Task 2:
Create a class Rectangle that represents a rectangle shape with the following attributes:
length (float)
width (float)
Add two methods:
area() that returns the area of the rectangle.
perimeter() that returns the perimeter of the rectangle.
Define the class and initialize the attributes.Implement area() and perimeter() methods.
Create an instance of Rectangle and test both methods.
'''

class Rectangle:
    def __init__(self, length, width):
        self.length=float(length)
        self.width=float(width)

    def area(self):
        return self.length*self.width

    def perimeter(self):
        return self.length+self.width


my_figure=Rectangle(5,4)

print(my_figure.area())
print(my_figure.perimeter())