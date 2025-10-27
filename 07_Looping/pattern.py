# Write a program to print the following star pattern. 
#   * 
#  *** 
# ***** for n = 3 
# Write a program to print the following star pattern: 
# * 
# ** 
# ***      for n = 3 
# Write a program to print the following star pattern. 
# * * * 
# *   *  
# * * * for n = 3 
n = 7

# First pattern
for i in range(1, n + 1):
    print(' '*(n-i),end="")
    print('*'*(2*i-1),end="")
    print("")

print()  # New line for separation

# Second pattern
for i in range(1, n + 1):
    print('*' * i)

print()  # New line for separation

# Third pattern
for i in range(n):
    if i == 0 or i == n - 1:
        print('* ' * n)
    else:
        print('*' + ' ' * (2 * (n - 1) - 1) + '* ')