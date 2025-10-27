# Write a recursive function to calculate the sum of first n natural numbers. 

# Recursive function to find sum of first n natural numbers
def sum_natural(n):
    if n == 1:
        return 1
    else:
        return n + sum_natural(n - 1)

print(sum_natural(10))
