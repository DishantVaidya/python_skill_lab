#Check that a tuple type cannot be changed in python. 

# Creating a tuple
my_tuple = (10, 20, 30)

print("Original tuple:", my_tuple)

# Trying to change one element
try:
    my_tuple[1] = 50
except TypeError as e:
    print("Error:", e)
