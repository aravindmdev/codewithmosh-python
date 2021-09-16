def greet(first_name, last_name):
    print("I'm a function")
    print("I need 2 line breaks after me")
    print(f"{first_name} {last_name}")


def greet_return(first_name, last_name):
    return f"{first_name} {last_name}"


def increment(num, by):
    return num + by


def increment_1(num, by=1):  # with optional parameter with default argument
    return num + by


def multiply(*numbers):  # this will take a collection as arument.
    total = 1
    # numbers will be of type tuple (immutable collection)
    for number in numbers:
        total *= number
    return total


def save_user(**user):  # takes multiple keyworg arguments
    print(user)  # it will be dictionary data type.
    print(user["id"])  # access the value


greet("Aravind", "Mohan")

message = greet_return("Aravind", "Mohan")

# we can give the parameter name along with the argument name. Called Keyword argument
print(increment(5, by=1))

save_user(id=1, name="Aravind", age=22)


#### Scope ####
msg = "a"


def scope_fun(name):
    msg = "b"  # This will considered local to the function. If it needs to be global it should be defined within function with prefix with "global"
    print(msg)


scope_fun("mosh")
print(msg)  # This will print "a"
