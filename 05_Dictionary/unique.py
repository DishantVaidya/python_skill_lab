# Write a program to input eight numbers from the user and display all the unique numbers (once). 
#set() creates empty set inside the variable , if we use {} it will create a list
set = set()

#User input from 1 to 8 numbers
for i in range(1,9):
    num = int(input("Enter the values upto 8:"))
    set.add(num) #appending the number to the set

#printing the set
print(set)    