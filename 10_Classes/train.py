# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) 
# and get fare information of train running under Indian Railways. 

class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def get_status(self):
        print(f"Train: {self.name}")
        print(f"Available Seats: {self.seats}")

    def fare_info(self):
        print(f"Train: {self.name}")
        print(f"Ticket Fare: Rs {self.fare}")

    def book_ticket(self):
        if self.seats > 0:
            print(f"Ticket booked! Your seat number is {self.seats}.")
            self.seats -= 1
        else:
            print("Sorry, train is full. No seats available.")

city = Train("Pune Express", 150, 5)
print("-"*20)
city.get_status()
print("-"*20)
city.fare_info()
print("-"*20)
city.book_ticket()
print("-"*20)
city.book_ticket()
print("-"*20)
city.get_status()
print("-"*20)
city.book_ticket()
print("-"*20)
city.book_ticket()
print("-"*20)
city.book_ticket()
print("-"*20)
city.get_status()
print("-"*20)
