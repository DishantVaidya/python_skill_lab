# Create a class “Programmer” for storing information of few programmers 
# working at Microsoft. 

class Programmer:
    company = "Microsoft"  
    def __init__(self, name, age, language, experience):
        self.name = name
        self.age = age
        self.language = language
        self.experience = experience

    def info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Language: {self.language}")
        print(f"Experience: {self.experience} years")
        print(f"Company: {self.company}")
        print("-" * 30)


# Creating few programmer objects
p1 = Programmer("Dishant", 20, "Python", 2)
p2 = Programmer("Riya", 22, "C++", 3)
p3 = Programmer("Arjun", 25, "JavaScript", 4)

# Displaying their information
p1.info()
p2.info()
p3.info()
