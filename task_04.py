"""
● Write a program that remove all vowels from the input word and
generate a brief version of it.
"""

vowels = ['o', 'u', 'i', 'e', 'a']
brief = ""
newString = input("Please enter the string: ").lower()
for i in range(len(newString)):
    if newString[i] not in vowels:
        brief = brief + newString[i]

print(brief)


