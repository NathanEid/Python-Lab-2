"""
● write a function that takes a number as an argument and if the
number divisible by 3 return "Fizz" and if it is divisible by 5 return
"buzz" and if is divisible by both return "FizzBuzz"
"""


def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        result = "FizzBuzz"
        return result
    elif num % 3 == 0:
        result = "Fizz"
        return result
    elif num % 5 == 0:
        result = "Buzz"
        return result
    else:
        result = "Not Divisible"
        return result


num = input("Enter the Number: ")
while True:
    if num.isdigit():
        num = int(num)
        break
    else:
        num = input("Please enter Number..> ")

result = fizzbuzz(num)
print(result)
