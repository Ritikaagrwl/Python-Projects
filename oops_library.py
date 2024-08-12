# oops library

class Library:
    
    def __init__(self,list_of_books,library_name):
        self.list_of_books = list_of_books
        self.library_name = library_name        
        self.lendDict = {}
       
    def display(self):
        print(f"\nThe available books in {self.library_name} are:")
        for item in self.list_of_books:
            print(item)
        print("")
        
    def lend_book(self,book,name):
        if book in self.list_of_books:
            if book not in self.lendDict.keys():
                print("Book is given to you.")
                self.lendDict.update({book:name}) 
            else:
                print(f"The {book} book you asked for is with {self.lendDict[book]}\nPlease lend another book.")
        else:
            print("Please enter the book present in the library")
        
    def add_book(self,book):
        self.list_of_books.append(book)
        print(f"Thanks for giving the book to {self.library_name}")
    
    def return_book(self,book):
        del self.lendDict[book]
        print(f"{book} book has been returned")

if __name__ == "__main__":
    ritika = Library(["Biology","Maths","Physics","Chemistry","English","Hindi"],"RitikaLibrary")
    
    while True:
        # print("Enter the task you want to perform from the following:\n1. Display Book\n2. Lend Book\n3. Add Book\n4. Return Book\nOr Enter q to exit the program.\n")
        
        action = input()
        
        if action == "q" or action == "Q":
            break
        
        elif action == "1" or action.capitalize() == "Display Book":
            ritika.display()
        
        elif action == "2" or action.capitalize() == "Lend Book":
            book = input("Enter the book you want to Lend: ")
            name = input("Enter your name")
            ritika.lend_book(book,name)
        
        elif action == "3" or action.capitalize() == "Add Book":
            book = input("Enter the book you want to add: ")
            ritika.add_book(book)
        
        elif action == "4" or action.capitalize() == "Return Book":
            book = input("Enter the book you want to return: ")
            ritika.return_book(book)
        
        else:
            print("Please enter from the given task only.")
            
        