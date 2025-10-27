# Write a program which finds out whether a given name is present in a list or not.

List = ["dishant","vaidya","dish"]
Name = input("Enter you name :").lower()

if Name in List:
    print("Your name is in list.")
else:
    print("Your name is not present in list.")    