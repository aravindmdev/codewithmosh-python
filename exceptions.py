try:
    age = int(input("Age: "))
except ValueError:
    print("Enter a valida age")
else:
    print("no exceptions encountered")
print("Execution continues")

try:
    age = int(input("Age: "))
except ValueError as ex:
    print("Enter a valida age")
    print(ex)  # this will have system error message
else:
    print("no exceptions encountered")

try:
    age = int(input("Age: "))
    x = 10/age
except (ValueError, ZeroDivisionError()):
    print("Enter a valida age")
else:
    print("no exceptions encountered")


try:
    file = open("app.py")
    age = int(input("Age: "))
    x = 10/age
except (ValueError, ZeroDivisionError()):
    print("Enter a valida age")
else:
    # will be executed when no exceptions are thrown
    print("no exceptions encountered")
finally:  # will be executed in any case
    file.close()

try:
    # file will be automatically closed. No need of finally statement.
    with open("app.py") as file:
        age = int(input("Age: "))
        x = 10/age
except (ValueError, ZeroDivisionError()):
    print("Enter a valida age")
else:
    print("no exceptions encountered")

# Raising an error


def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be less than 0")
    return 10/age


try:
    calculate_xfactor(-1)
except ValueError as Error:
    print(Error)
