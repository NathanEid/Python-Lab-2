"""
● Write a program that prints the locations of "i" character in any
string you added.
"""
l = []
newString = input("Please enter the string: ").lower()
for i in range(len(newString)):
    if newString[i] == "i":
        l.append(i)

print("Indexes of i character is: ")
print(l)
