"""
● Write a program that build a Mario pyramid like below:
"""
num = input("Enter the number: ")
if num.isdigit():
    num = int(num)+1
    for i in range(num):
        for j in range(i):
            print("* ", end="")
        print()

    s = num*2 - 2

    for i in range(num):
        for k in range(s):
            print(end=" ")
        s -= 2
        for j in range(i):
            print("* ", end="")
        print()

else:
    print("That is not a number.")
