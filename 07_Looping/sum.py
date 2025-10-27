# Write a program to find the sum of first n natural numbers using while loop

# Get input from user
n = int(input("Enter a number: "))

# Initialize variables
sum = 0
i = 1

# Calculate sum using while loop
while i <= n:
    sum += i
    i += 1

# Print the result
print(f"The sum of first {n} natural numbers is: {sum}")