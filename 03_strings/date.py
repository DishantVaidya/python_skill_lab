#Write a program to fill in a letter template given below with name and date.
'''
letter =
Dear <|Name|>, 
You are selected! 
<|Date|> 
''' 
# #option 1
name = input("Enter your name :")
date = input("Enter a date :")
letter = f"Hello {name}, \n You are selected !! \n Join us at {date}"

print(letter)

#option 2
letter = '''  
Dear <|Name|>, 
You are selected! 
<|Date|> 
''' 

print(letter.replace("<|Name|>","Dishant").replace("<|Date|> ","30th November"))