"""
● Ask the user for his name then confirm that he has entered his
name(not an empty string/integers). then proceed to ask him for
his email and print all this data (Bonus) check if it is a valid email
or not
"""
import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


def getinfo():
    name = input("Enter Your Name Please: ")
    while True:
        if name.isalpha():
            chemail = input("Enter Your email Please: ")
            while True:
                if (re.fullmatch(regex, chemail)):
                    email = chemail
                    break
                else:
                    chemail = input("Enter a valid email Please: ")
            break
        else:
            name = input("Please enter a valid name: ")
    info = (name, email)

    return info

data = getinfo()
print(f" The Name is: {data[0]}")
print(f" The Email is: {data[1]}")
