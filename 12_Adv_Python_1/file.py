# Write a program to open three files 1.txt, 2.txt and 3.txt if any these files are not 
# present, a message without exiting the program must be printed prompting the same.

for i in range(1,4):
    try:
        with open(f"{i}.txt", "r") as f:
            print(f.read())
    except Exception as e:
        print(e)

print("Thank You........")