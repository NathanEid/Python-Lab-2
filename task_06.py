"""
● Write a program that generate a multiplication table from 1 to the
number passed.
"""
biglist = []
num = input("Enter the number: ")
if num.isdigit():
    num = int(num)+1
    for i in range(1, num):
        sublist = []
        for j in range(1, i+1):
            sublist.append(j*i)
        biglist.append(sublist)

    print(biglist)
else:
    print("That is not a number.")
