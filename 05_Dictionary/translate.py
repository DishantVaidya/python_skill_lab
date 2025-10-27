# Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up! 

#Creating dictionary with translation
translate={
            "hello":"Namaste",
            "good":"Accha",
            "how":"Kaise",
            "cat":"billi"
           }
#taking input from user 
word = input("Enter the word you want :").lower() #this will lowercase the string to avoid caps error

print(translate[word])