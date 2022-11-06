# Your parking garage class should have the following methods:
# - takeTicket
# - This should decrease the amount of tickets available by 1
# - This should decrease the amount of parkingSpaces available by 1
# - payForParking
# - Display an input that waits for an amount from the user and store it in a variable
# - If the payment variable is not empty then (meaning the ticket has been paid) -> display a message to the user that their ticket has been paid and they have 15mins to leave
# - This should update the "currentTicket" dictionary key "paid" to True
# -leaveGarage
# - If the ticket has been paid, display a message of "Thank You, have a nice day"
# - If the ticket has not been paid, display an input prompt for payment
# - Once paid, display message "Thank you, have a nice day!"
# - Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
# - Update tickets list to increase by 1 (meaning add to the tickets list)

# You will need a few attributes as well:
# - tickets -> list
# - parkingSpaces -> list
# - currentTicket -> dictionary


class parkingGarage():
    def __init__(self, tickets, parkingSpaces, currentTicket, capacity = 5, licensePlate = ''):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTicket = currentTicket
        self.licensePlate = licensePlate
        self.capacity = capacity
        

    def takeTicket(self):
        if len(self.parkingSpaces) == self.capacity:
            print("Parking lot is full. Try again later.")
        else:
            self.licensePlate = input("What is your license plate?"  )
            self.currentTicket[self.licensePlate] = "unpaid"
            self.tickets.append(0)
            self.parkingSpaces.append(0)

    def payForParking(self):
        while True:
            self.licensePlate = input("What is your license plate?"  )
            payment = input("Please pay $5.00 to validate ticket.   yes/no  ")
            if payment.lower() == "yes":
                self.currentTicket[self.licensePlate] = "paid"
                print("Your ticket has been paid, please exit within 15 minutes.")
                break
            elif payment.lower() == "no":
                print("Payment failed.")
                break
            else:
                print("Invalid input.")

    
    def leaveGarage(self):
        self.licensePlate = input("What is your license plate?"  )
        if self.currentTicket[self.licensePlate] == "paid":
            print("Thank You, have a nice day!")
            del self.tickets[0]
            del self.parkingSpaces[0]
        elif self.currentTicket[self.licensePlate] == "unpaid":
            print("Please pay before exiting.")
        else:
            "No car with that license plate is in this garage."

def run():
    while True:
        prompt = input('What would you like to do? enter/pay/leave/quit   ')
        if prompt.lower() == "enter":
            my_Garage.takeTicket()
        elif prompt.lower() == 'pay':
            my_Garage.payForParking()
        elif prompt.lower() == 'leave':
            my_Garage.leaveGarage()
        elif prompt.lower() == 'quit':
            break
        else:
            print("Invalid input, try again.")

my_Garage = parkingGarage([],[],{})
run()








