# Lists
from sys import getsizeof
from array import array
from collections import deque  # Import the deque class
letters = ["a", "b"]
print(letters[0])  # Accessing the values

matrix = [[0, 1], [1, 0]]

zeros = [0] * 5  # creates a list with 5 zeros

combined = zeros + letters  # combines both to one list

numbers = list(range(20))  # list of 0 to 19
print(numbers[::2])  # print every other element. like 0, 2, 4...
print(numbers[::-1])  # print the list in the reverse order

chars = list("Aravind")  # list of chars in the string

num = [1, 2, 3]
first, second, third = num  # assigns each value to the variable.

num_2 = [2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]
first, second, *other = num_2  # takes first two values and rest to others as list
first, *other, last = num_2  # this also works
print(other)

letters = ["a", "b", "c"]

for letter in letters:
    print(letter)

for letter in enumerate(letters):
    print(letter[0], letter[1])  # enumerate will give index and value as tuple

# Cleaner
for index, letter in enumerate(letters):
    print(index, letter)

# Add
letters.append("d")
letters.insert(0, "-")  # inserts the value at a sepcific index

# Remove
letters.pop()  # removes last one
letters.pop(1)  # removes at a specific index
# removes by value. But will remove only the first instance
letters.remove("b")
del letters[0:2]  # removes a range
letters.clear()  # clears the whole lists
letters.count("a")  # counts the item

if "d" in letters:
    # returns the index. If the value is not there it will throw error. So used the if condition
    print(letters.index("d"))

numbers = [1, 2, 3, 4, 5]

numbers.sort()  # sorts the list in asc but modifys the original one
numbers.sort(reverse=True)  # sorts in desc
sorted(numbers)  # will return a new list
sorted(numbers, reverse=True)  # sorts in desc

# what if the items areof different kinds
items = [
    ("product1", 20),
    ("product2", 10),
    ("product3", 30)
]


def item_sort(item):
    return item[1]  # On what the sorting should be done


items.sort(key=item_sort)  # will sort based on the price

# using cleaner lambda functions
items.sort(key=lambda item: item[1])  # lambda parameter:expression

# Map function
items = [
    ("product1", 10),
    ("product2", 20),
    ("product3", 30)
]

prices = []
# Take only the prices to a new list
for item in items:
    prices.append(item[0])

# Using map function
# Map function returns map object which is iterable. So converting to List
prices = list(map(lambda item: item[1], items))

# Filter function
# filter returns item from items based on lambda func which return boolean.
# filter func return iterable filter object
filtered = list(filter(lambda item: item[1] >= 10, items))

# List comprehension
# Same as using map function. This is the preferred method. More performance
prices = [item[1] for item in items]

# Same as using filter functions
filtered = [item for item in items if items[1] >= 10]

# merge two lists with 1:1 grouping
list1 = [1, 2, 3]
list2 = [10, 20, 30]

# Output: [('a', 1, 10), ('b', 2, 20), ('c', 3, 30)]
merged_list = list(zip("abc", list1, list2))

# Implementing stack using list - LIFO
session = []  # Stack
session.append(1)  # Inserts value to stack
session.pop()  # remove the last value
if not session:  # checks if stack is empty
    print("empty")
else:
    session[-1]  # gets the last value in the stack

# Implementing queues

queue = deque([])  # Intialize the queue list
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()  # pops the first value
if not queue:
    print("Empty")

# Tuple - Immutable lists. Enclosed in ()
point = (1, 3)
point = 1, 3
point = 1,  # if comma is not put it will treat it as an integer
# converts lists to a tuple. Takes an iterable as argument
point = tuple([1, 3])

# Swapping numbers
x = 10
y = 11

x, y = y, x  # The RHS is a tuple. And its getting unpacked to LHS

# Arrays
# When dealing with large sets. List could be slower
# i = typecode. In this case an integer. Array can hold only one data type.
numbers = array("i", [1, 2, 4])


# Sets - list with no duplicates
# Cannot use index to access values
numbers = [1,  1, 2, 3, 4]
first = set(numbers)
second = {1, 5}

print(first | second)  # union
print(first & second)  # intersection
print(first - second)  # minus
# returns the ones which are available only on one set (semantic difference)
print(first ^ second)

if 1 in first:
    print("yes")

# Dictionary
point = {"x": 1, "y": 1}
point = dict(x=1, y=2)  # better way
point["x"] = 10
point["z"] = 20  # Assign values

if "a" in point:
    print(point["a"])

print(point.get("a", 0))  # Better, default value of 0 if not found.

del point["x"]

for key in point:  # itertes through key
    print(key, point[key])

for key, value in point.items():  # returns key value tuple.
    print(key, value)

# creates the dictionary using comprehension
values = {x: x*2 for x in range(5)}

# Generator expressions
# Memory efficient. Size of values will be constant irrespective of range size. Len() will not work
values = (x * 2 for x in range(10))  # 10 or 100 size of values will be same

getsizeof(values)  # will be constant for generator expressions.

# Unpacking operator
# List
values = list(range(5))
values = [*range(5)]  # Same as above
values = [*range(5), *"Hello"]  # combine two
# Dictionary
first = {"x": 1}
second = {"x": 10, "y": 2}
combined = {**first, **second, "z": 1}
