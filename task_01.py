"""
● Write a function that accepts two arguments (length, start) to
generate an array of a specific length filled with integer numbers
increased by one from start.
"""

def fillArray(length, start):
    arr = []
    i = 0
    while i < length:
        arr.append(start)
        start += 1
        i += 1
    print(arr)

length = input("Enter the length of the array: ")
while True:
    if length.isdigit():
        length = int(length)
        break
    else:
        length = input("Please enter Number..> ")

start = input("Enter the start of the array: ")
while True:
    if start.isdigit():
        start = int(start)
        break
    else:
        start = input("Please enter Number..> ")

fillArray(length, start)
