#Write a program to detect double space in a string.
# Input string from user
text = input("Enter a string: ")

# Check for double spaces
if "  " in text:
    print("Double space detected!")
else:
    print("No double spaces found.")


'''OR YOU CAN USE .FIND("  ") FNCTION TO FIND INDEX'''
print(text.find("  "))