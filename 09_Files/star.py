# Write a program to read the text from a given file ‘poems.txt’ and find out 
# whether it contains the word ‘twinkle’. 

with open("poem.txt") as f:
    content = f.read()
    if "twinkle" in content:
        print("Present")
    else:
        print("Not present")