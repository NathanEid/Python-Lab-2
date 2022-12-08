"""
● Write a program that counts up the number of
vowels [a, e, i, o,u] contained in the string.
"""

vowels = ['o', 'u', 'i', 'e', 'a']
count = 0
newString = input("Please enter the string: ").lower()
for i in range(len(newString)):
    for j in range(len(vowels)):
        if newString[i] == vowels[j]:
            count += 1

if count == 0:
    print("there is no vowels.")
else:
    print("the count of vowels is: " + str(count))
