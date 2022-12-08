"""
Fill an array with 5 elements from the user, Sort it in descending
and ascending orders then display the output.
"""

elements = []
for i in range(1, 6):
    num = input("Please enter the element number " + str(i) + " :")
    
    if num.isdigit():
        elements.append(int(num))
    else:
        print("it's not a digit, it can't added to the list")

print("The Elements you entered: ")
print(elements)

print("The Elements you entered ascending order: ")
elements.sort()
print(elements)

print("The Elements you entered descending order: ")
elements.sort(reverse=True)
print(elements)
