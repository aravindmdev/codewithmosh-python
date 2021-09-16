# Declaration
class Point:
    def draw(self):  # functions should have atleast one argument. Self refers to the current object
        print("draw")


point = Point()
# check whether an object is an instance of the class.
print(isinstance(point, Point))


class Point2:
    default_color = "red"  # class level attribute. will be shred across all instances

    def __init__(self, x, y):  # Constructor - will be called when the object is created. Self will be automatically passed by Python
        self.x = x  # instance level attributes. Ca be different for each object
        self.y = y

    def draw(self):  # functions should have atleast one argument. Self refers to the current object
        print(f"Point ({self.x}, {self.y})")


# calling the class level attribute directly using class. No need of instance.
print(Point2.default_color)

point2 = Point2(1, 2)
point2.draw()

# Class methods


class Point3:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod  # method created at a class. Can be used to create an object with specific initial values
    def zero(cls):  # giving cls is convention
        return cls(0, 0)  # returns a point objcet with 0, 0 initial values


point3 = Point3.zero()  # returns a point object with the initial values

# Magic methods are inherited methods in a class which serves specific purpose
# For eg: __init__ is the constructor which is automatically called when an object is created.
# We can override that to create some initializations.
# Similarly __str__ is invoked when an object is tried to be converted to a string. We can override that.


class Point4:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):  # Invoked when objects are converted to string
        return (f"({self.x},{self.y})")


point4 = Point4(1, 2)
# This will print (1,2). If __str__ was not overriden then it would print the memory address.
print(point4)
point41 = Point4(1, 2)
print(point4 == point41)  # equality will invoke the __eq__ magic method
