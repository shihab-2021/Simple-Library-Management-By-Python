class User:
    def __init__(self, name, roll, password) -> None:
        self.name = name
        self.roll = roll
        self.password = password
        self.borrow_books = []
        self.return_books = []

class Library:
    def __init__(self, book_list) -> None:
        self.book_list = book_list
    
    def borrow_book(self, bookName, user):
        for book in self.book_list:
            if book == bookName:
                if bookName in user.borrow_books:
                    print("You already have this book!!! Please return the book. ")
                    return
                if self.book_list[book] == 0:
                    print("This book is not available right now!!!")
                    return 
                self.book_list[book] -= 1
                user.borrow_books.append(bookName)
                print("Book borrowed successfully!!!")
                return
        print("Invalid book request, not available in this library!!!")

    def return_book(self, bookName, user):
        for book in self.book_list:
            if book == bookName:
                self.book_list[book] += 1
                user.borrow_books.remove(bookName)
                user.returned_books.append(bookName)
                print("Book returned successfully!!!")
                return   
            else:
                print("You never borrowed this book from us!!!")
                return
        print("Are you sure? This book is not from our library!!!")

    def donate(self, bookName, amount):
        for book in self.book_list:
            if book == bookName:
                self.book_list[book] += amount
                print("Thanks for your donation!!!")
                return
        self.book_list[bookName] = amount
        print("Thanks for your donation!!!")
    
    def availability(self):
        for book in self.book_list:
            if self.book_list[book] > 0:
                print(book, self.book_list[book])

library = Library({"English": 2, "Bangle": 5, "Math": 3 })
allUsers = []
currentUser = None

while True:
    if currentUser == None:
        print("Not logged in \nPlease Login or Create account (L/c)")
        option = input()
        if option == "L":
            roll = int(input("Roll: "))
            password = input("Password: ")
            match = False
            for user in allUsers:
                if user.roll == roll and user.password == password:
                    currentUser = user
                    match = True
                    break
            if match == False:
                print("User not found")
        else:
            name = input("Name: ")
            roll = int(input("Roll: "))
            password = input("Password: ")
            found = False
            for user in allUsers:
                if user.roll == roll:
                    print("This account is already  exist!!!")
                    found = True
                    break
            if found == True:
                continue
            user = User(name, roll, password)
            currentUser = user
            allUsers.append(currentUser)
    else:
        print("\nOptions")
        print("-------")
        print("1. Borrow a book")
        print("2. Return a book")
        print("3. Borrow book list")
        print("4. Return book list")
        print("5. Check availability")
        print("6. Donate")
        print("7. Logout")
        x = int(input("Give option: "))
        print("\n")
        if x==1:
            bookName = input("Book name: ")
            library.borrow_book(bookName, currentUser)
        elif x==2:
            bookName = input("Book name: ")
            library.return_book(bookName, currentUser)
        elif x==3:
            print(currentUser.borrow_books)
        elif x==4:
            print(currentUser.return_books)
        elif x==5:
            library.availability()
        elif x==6:
            bookName = input("Book name: ")
            amount = int(input("Amount: "))
            library.donate(bookName, amount)
        elif x==7:
            currentUser = None