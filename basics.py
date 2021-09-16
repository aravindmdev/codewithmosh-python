# string concatenation
first = "Aravind"
last = "Mohan"
full = f"{first} {last}"  # formatted string
full = f"{len(first)} {last}"
print(full)

# string functions #################
course = "python programming"
print(course.upper())
print(course.lower())

print(course.title())  # Capitalizes the first letter

# Trim spaces on both sides, lstrip and rstrip also available
print(course.strip())

# returns starting index. Case sensistive. -1 if not found
print(course.find("pro"))

print(course.replace("pro", "sos"))

print("pro" in course)  # returns boolean based on presence
print("pro" not in course)  # returns boolean based on presence

# Numbers
print(2 + 3j)  # Complex numbers
print(10 // 3)  # Retunrs integer. Quotient part
print(10 ** 3)  # Exponentials

# for more math functions do "import math"

# Type conversion
# x = input("X: ")  # takes input from the user
x = 2
print(type(x))  # prints the datatype
y = int(x) + 1  # COnverts x to an integer.

# Falsy values "", 0 and None

# Conditional Statements
temp = 15

if temp == 15:
    print("Its 15")
elif temp == 20:
    print("Its 20")
else:
    print("its something else")

# Ternary operator
age = 22

message = "Eligible" if age > 12 else "not eligible"
print(message)

# Chaining comparison operator
if 18 <= age < 65:
    print("eligible")

# Loops
for n in range(1, 10, 2): # (Starting, < end number, step)
    print("print", n, n * "*")

successful = False
for n in range(3):
    print("Attempt", n + 1) 
    if successful:
        print("Successful")
        break
else: # This else is for the for loop. Executes only if the loop is not terminated in between
    print("Attempted 3 times and failed")


number = 100
while number > 0:
    print(number)
    number //= 2


# Iterabels

# range(5) returns a range object

# strings are iterables
for x in "python":
    print(x)

