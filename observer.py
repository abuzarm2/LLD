#user class
class User:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def alert(self,message):
        print(f"Dear {self.first_name} {self.last_name}, {message}")

class Amazon:
    def __init__(self):
        self.users = []
        self.events = []
    
    def addUser(self, user):
        self.users.append(user)
        print(f"{user.first_name} added successfully!!")
    
    def notify(self,message):
        for user in self.users:
            user.alert(message)
    
    def addEvents(self, name, date, message):
        print("Creating Event")
        self.events.append([name , date])
        print("Event Created Successfully")
        self.notify(message)
        
u1 = User("Abuzar","Mulla")
u2 = User("Alex", "Mercer")
u3 = User("John", "Doe")

amazon = Amazon()
amazon.addUser(u1)
amazon.addUser(u2)
amazon.addUser(u3)

amazon.addEvents("Christmas Sale", "25th Dec", "Pick your Deal, 50% OFF, HURRY!!!")
