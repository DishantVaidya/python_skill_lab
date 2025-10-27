# # Write a program to find the greatest of four numbers entered by the user. 
#Program without if else
# Num = []
# for i in range(1,5):
#     n=int(input("Enter the number:"))
#     Num.append(n)
# print("Greatest number of 4 number is ",max(Num))    

n1 = int(input("Enter the number :"))
n2 = int(input("Enter the number :"))
n3 = int(input("Enter the number :"))
n4 = int(input("Enter the number :"))

if n1>n2 and n1>n3 and n1>n4:
    print("Greatest number is:", n1)
elif n2>n1 and n2>n3 and n2>n4:
    print("Greatest number is:", n2)
elif n3>n1 and n3>n2 and n3>n4:
    print("Greatest number is:", n3)
else:
    print("Greatest number is:", n4)
