#create a class called Car with attributes brand and color. Instantiate an object of the Car class and print its attributes.

class car:
        def __init__(self, brand, color):#we defined the attributes asked for
          self.brand = brand 
          self.color = color 

my_car = car(brand="Range Rover", color="Pink") 

print(f"Brand: {my_car.brand}") #these are the attributes identified
print(f"Color: {my_car.color}")

    

#Add a method called start-engine to the Car class that prints a message saying the negine of the car started.
# Create an instance of Car and call the method.

class Car:
    def __init__(self, brand, color):
        self.brand = brand 
        self.color = color 

    def start_engine(self):
        print(f"The engine of the {self.brand} {self.color} car has started!")
        
my_car = Car(brand="Range Rover", color="Pink")

my_car.start_engine()


#Create a class called BankAccount with attributes account-number and balance.Add methods to:
#Deposit an ammouunt
#withdraw an amount (only if suffient balance exits).
#print the account balance.

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number 
        self.balance = balance 

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        elif amount > 0:
            print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def print_balance(self):
        print(f"Account balance: {self.balance}")

account = BankAccount(account_number="123456789")

account.deposit(500)

account.withdraw(200)

account.print_balance()

    

#implement a class called Library that manages a collection of books. Each book has a title , author, and available status.
# The Library class should have methods to:
#Add a book to the library
#Remove a book from the library
#Check if a book is available by title
#Borrow a book (mark it as unvailable if it's not  availabe)
#Return a book (mark it as available again if it was borrowed)

class Library:
    class Book:
        def __init__(self, title, author, available_status=True):
            self.title = title 
            self.author = author  
            self.available = available_status 

        def __str__(self):
            return f"'{self.title}' by {self.author}, Available: {self.available}"

    def __init__(self):
        self.books = [] 

    def add_book(self, title, author):
    
        new_book = self.Book(title, author)
        self.books.append(new_book)
        print(f"Added: {new_book}")

    def remove_book(self, title):
    
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"Removed: {book}")
                return
        print(f"Book with title '{title}' not found.")

    def is_available(self, title):
        
        for book in self.books:
            if book.title == title:
                return book.available
        print(f"Book with title '{title}' not found.")
        return False

    def borrow_book(self, title):
        
        for book in self.books:
            if book.title == title:
                if book.available:
                    book.available = False
                    print(f"You borrowed: {book}")
                    return
                else:
                    print(f"'{title}' is currently unavailable.")
                    return
        print(f"Book with title '{title}' not found.")

    def return_book(self, title):
        
        for book in self.books:
            if book.title == title:
                if not book.available:
                    book.available = True
                    print(f"You returned: {book}")
                    return
                else:
                    print(f"'{title}' was not borrowed.")
                    return
        print(f"Book with title '{title}' not found.")

    def print_books(self):

        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(book)

library = Library()

library.add_book("2006", "Jenny Nimmo")
library.add_book("Tell me your Secret", "Sidney Sheldon")
library.add_book("Tonny And Josephin", "Whitney Josephin")
library.add_book("Animal Farm", "George Orwell")

library.print_books()

library.borrow_book("2006")

print("Is '2006' available?", library.is_available("2006"))

library.return_book("2006")

library.remove_book("To Kill a Mockingbird")

library.print_book()





