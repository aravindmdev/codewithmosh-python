# Declaration
from collections import namedtuple
from abc import ABC, abstractmethod


class Point:
    def draw(self):  # functions should have atleast one argument. Self refers to the current object
        print("draw")


point = Point()
# check whether an object is an instance of the class.
print(isinstance(point, Point))


class Point2:
    default_color = "red"  # class level attribute. will be shared across all instances

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

    # Override and implement the equality according to us.
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


point4 = Point4(1, 2)
# This will print (1,2). If __str__ was not overriden then it would print the memory address.
print(point4)
point41 = Point4(1, 2)
print(point4 == point41)  # equality will invoke the __eq__ magic method


# Implementing a class with different functionalities
# Private attributes. Prefix with __
# Technically we still can access private attributes. Get the hidden name from <object>.__dict__
# Python does not complete private setting. Its not about security. Its just warning.

class TagCloud:
    def __init__(self):
        self.__tags = {}  # Initializes a dictionary

    def add(self, tag):
        # Checks if entry is there, if not 0, then add 1 to that.
        # .lower is used to avoid case sensistivity
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)  # returns count of tag

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


cloud = TagCloud()  # Create the object
cloud.add("Python")
cloud.add("python")
cloud.add("PYthon")
cloud["python"]  # this invokes __getitem__ magic method
cloud["python"] = 10  # invokes __setitem__ magic method
len(cloud)  # invokes __len__ magic method
for tag in cloud:  # invokes the __iter__ method
    print(tag)

# Get Set Properties

# This implementation is not pythonic


class Product1:
    def __init__(self, value):
        self.set_price(value)

    def get_price(self):
        return self.__price

    def set_price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value


product1 = Product1(-10)
product1.set_price(-20)
product1.get_price()

# Pythonic implementation of above code


class Product2:
    def __init__(self, value):
        self.price = value

    @property
    def price(self):  # the attribute name will be the function name
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value


product2 = Product2(-10)
product2.price = -20  # now the price can be accessed as an attribute

# Inheritance


class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


# Inherits Animal class. to inlcude multiple separate with commas.
# During multiple inheritance if both the class have the same methods then the method from the class given first will be executed.
class Mammal(Animal):
    # to call the contructor of the parent class. This is not needed if the child class does not have constructor.
    super.__init__()

    def __init__(self):
        self.weight = 2  # this will override the Animal constructor.

    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


m = Mammal()
f = Fish()

print(m.age)  # will print 1
m.eat()
f.eat()

# Some in-built functions
print(isinstance(m, Mammal))  # will be true
print(isinstance(m, object))  # all classes inherit from object class
# checks whether the class inherits from another
print(issubclass(Mammal, Animal))


# Proper inheritance, Abstract class and custom exception
# To create abstract class and methods define this "from abc import ABC, abstractmethod"
# Custom exception


class InvalidOperationError(Exception):
    pass


class Stream(ABC):  # ABC - Abstract base class. To create the abstract method
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already opened")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed")
        self.opened = False

    @abstractmethod  # decorator for the abstract method
    def read(self):
        # No implemenation. Whichever class inherits the stream class needs to implement this.
        # Otherwise the object cannot be created for the child class.
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from the file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from the network")

# Polymorphism


class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("TextBox")


class DropDown(UIControl):
    def draw(self):
        print("DropDown")


def draw(control):  # this method which all controls are going to be executed. Mnay forms - Polymorphism
    control.draw()


TB = TextBox()
DD = DropDown()

# Even if the classes dont inherit UIControl it works. The draw function just passes the object and as long it is iterable it will work.
# Achieving polymorphism without inheritance is called Duck Typing.
draw([TB, DD])

# namedtuple - from collections import namedtuple
# can be used to repreesnt data classes
# immutable. If we wnat chnage values recrate the object
Point = namedtuple("Point", ["x", "y"])
p1 = Point(x=1, y=2)
p1 = Point(x=2, y=3)  # to change the values
# will return true. No need to implement the magic method __eq__
p2 = Point(x=2, y=3)
