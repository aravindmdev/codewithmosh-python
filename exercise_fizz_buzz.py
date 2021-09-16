def fizz_buzz(val):
    # 3 Fizz 5 Buzz 15 FizzBuzz
    if (val % 3 == 0) and (val % 15 == 0):
        return "FizzBuzz"
    if (val % 3 == 0):
        return "Fizz"
    if (val % 5 == 0):
        return "Buzz"
    return val


print(fizz_buzz(7))
