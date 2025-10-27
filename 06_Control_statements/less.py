# Write a program to find whether a given username contains less than 10 
# characters or not. 

username = input("Enter the username:")
len=len(username)

if len<10:
    print("Username shorter than 10 characters..")
else:
    print("perfect..")    