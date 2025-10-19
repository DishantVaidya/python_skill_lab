#Write a program to accept marks of 6 students and display them in a sorted manner.

#create empty list to store values first
Marks=[]

n=int(input("Total number of students:"))

for i in range(1,n+1):
    x=int(input("Give marks :"))
    Marks.append(x)

print("Sorted marks list :",sorted(Marks))    

#or you can do it directly 
Mark=[35,78,24,95,34,74]

print("Sorted marks list :",sorted(Mark))