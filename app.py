import json

FILE_NAME = "library.txt"

def load_books():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError , json.JSONDecodeError):
        return []

def save_books(books):
        with open(FILE_NAME, "w") as file:
            json.dump(books, file, indent=4)

def display_menu():
        print("\nWelcome to your Personal Library Manager!")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")

def add_book(books):
            title = input("Enter the book title: ").strip()
            author = input("Enter the author: ").strip()

            try:
                year =int(input("Enter the publication year: ").strip())
            except ValueError:
                print("Invalid year. Please enter a valid integer.")
                return
            
            genre = input("Enter the genre: ").strip()

            read_status = input("Have you read this book? (yes/no):").strip().lower() =="yes"

            books.append({
                "title": title,
                "author": author,
                "year": year,
                "genre": genre,
                "read": read_status
            })              

            save_books(books)
            print("Book added succesfully!")

def remove_book(books):
                title = input(" Enter the title of the book to remove: ").strip()

                updated_books = [book for book in books if book["title"].lower() != title.lower()]
                if len(updated_books) == len(books):
                    print("Book not found.")

                else: 
                    save_books(updated_books)
                    print("Book removed successfully!")

def search_books(books):
                print("search by:")
                print("1. Title")
                print("2. Author")
                choice = input("Enter your choice (1/2): ").strip()

                if choice == "1":
                    query = input("Enter the title: ").strip().lowe()
                    results = [book for book in books if query in book ["title"].lower()]
                elif choice == "2":
                    query = input("Enter the author: ").strip().lower()
                    results = [book for book in books if query in book["author"].lower()]
                else:  
                    print("No matching books found.")
                
def display_books(books):
                if not books:
                   print("No books in the library.")
                   return
                
                print("\nYour Library:")
                for idx, book in enumerate(books, start=1):
                    print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book ['read'] else 'Unread'}")

def display_statistics(books):
                total_books = len(books)
                read_books = sum(1 for book in books if book ["read"])

                print("n\Library Statistics:")
                print(f"Total books: {total_books}")

                if total_books > 0:
                    print(f"Percentage read: {read_books / total_books * 100:.2f}%")            
                else: 
                    print("Percentage read:0.00%")
def main():
    books = load_books()

    while True:
        display_menu()
        choice = input("Enter your choice (1-6):").strip()

        if choice == "1":
            add_book(books)
        elif choice == "2":
            remove_book(books)
            books = load_books()
        elif choice == "3":
            search_books(books)
        elif choice == "4" :
            display_books(books)
        elif choice == "5" :
            display_statistics(books)
        elif choice == "6":
            print("Library saved to file. Goodbye!")
            save_books(books)
            break
                    

        else:
            print("Invalid choice. Please select a valid option.")
                
                
if __name__ =="__main__":
    main()                                    

             