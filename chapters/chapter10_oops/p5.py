'''
Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats)
and get fare information of train running under Indian Railways.

'''
class Train:
    def __init__(self, name, seats, fare):
        self.name = name
        self.seats = seats
        self.fare = fare

    def bookTicket(self):
        if (self.seats > 0):
            print("Ticket booked successfully")
            self.seats -= 1
        else:
            print("Sorry, no seats available")

    def getStatus(self):
        print(f"Seats available: {self.seats}")

    def getFareInfo(self):
        print(f"Fare is ₹{self.fare}")


# object creation
p1 = Train("Indian Railways Express", 5, 450)

p1.getStatus()
p1.bookTicket()
p1.getFareInfo()
