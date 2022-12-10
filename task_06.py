"""
● Write a program which repeatedly reads numbers until the user
enters “done”.
○ Once “done” is entered, print out the total, count, and
average of the numbers.
○ If the user enters anything other than a number, detect their
mistake, print an error message and skip to the next number.
"""

def calc():
    sum = 0
    count = 0
    avg = 0
    while True:
        num = input("Enter Number, and done for End: ")
        if num.isdigit():
            num = int(num)
            sum += num
            count += 1
        elif num == "done":
            avg = sum / count
            print(f"The Sum of This Numbers: {sum}")
            print(f"The Count of This Numbers: {count}")
            print(f"The Average of This Numbers: {avg}")
            break
        else:
            print("Error, you should enter numbers or done for End.")
            continue

calc()

