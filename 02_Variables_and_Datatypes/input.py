# Check the type of variable assigned using input () function. 

Integer = int(input("Enter a number :")) #User input for Integer datatype using "int"
String = input("Enter a word :") #User input for string (Input function accept values in str by default)
Float = float(input("Enter a number with decimal :")) #User input for Flaot datatype using "float"

print(f"Your given number is {Integer} and its type is {type(Integer)}") # Printing values and type
print(f"Your given string is {String} and its type is {type(String)}")   # By using type() function
print(f"Your given number with decimal is {Float} and its type is {type(Float)}")