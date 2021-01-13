#!/usr/bin/python3

for fizz in range(100):
    if fizz % 15 ==0:
        print("FizzBuzz")
        continue
    elif fizz % 3 == 0:
        print("Fizz")
        continue
    elif fizz % 5 ==0:
        print("Buzz")
        continue
    print(fizz)
