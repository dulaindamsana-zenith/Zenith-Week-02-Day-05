# FizzBuzz Game

for number in range(1, 101):
    counter = number
    if counter % 3 == 0 and counter % 5 == 0:
        print("FizzBuzz")

    if counter % 3 == 0:
        print("Fizz")

    elif counter % 5 == 0:
        print("Buzz")

    else:
        print(number)