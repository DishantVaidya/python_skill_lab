# A spam comment is defined as a text containing following keywords: 
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program 
# to detect these spams. 

text = input("Enter the message :").lower()
spam = ["make a lot of money","buy now","subscribe this","click this"]

if any(phrase in text for phrase in spam):
    print("spam detected.....")
else:
    print("Safe message")    