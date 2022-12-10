"""
● Write a function which has an input of a string from user then it
will return the same string reversed.
"""


def reversedstring():
    s = input("Enter the string: ")
    while True:
        if s.isalpha():
            n = len(s)-1
            newstr = ""
            while n >= 0:
                newstr = newstr + s[n]
                n -= 1
            break
        else:
            s = input("Please enter String..> ")
    return newstr


mystr = reversedstring()
print(f"the reversed string is : {mystr}")
