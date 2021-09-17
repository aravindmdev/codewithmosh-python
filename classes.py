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
