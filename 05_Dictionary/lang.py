# Create an empty dictionary. Allow 4 friends to enter their favorite language as 
# value and use key as their names. Assume that the names are unique. 

#Empty dictionary
dict = {}

#loop for 4 friends
for i in range(1,5):
    Name = input("Enter the name :")
    Lang = input("Enter the language :")
    dict.update({Name:Lang})
    
#printing the dictionary
print(dict)    