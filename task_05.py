"""
Write a function that takes a string and prints the
longest alphabetical ordered substring occurred For example, if
the string is 'abdulrahman' then the output is: Longest substring in
alphabetical order is: abdu
"""
def alphabetecal():
    s = input("Enter the string: ")
    while True:
        if s.isalpha():
            longest = s[0]
            current = s[0]
            for c in s[1:]:
                if c >= current[-1]:
                    current += c
                    if len(current) > len(longest):
                        longest = current
                else:
                    current = c
            break
        else:
            s = input("Please enter String..> ")

    print("Longest substring in alphabetical order is:", longest)

alphabetecal()
