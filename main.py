# Book Library Manager

library = []

# Function to add a book
def add_book():
    print("\n📘 Add a New Book")
    title = input("Title: ").strip()
    author = input("Author: ").strip()
    year = int(input("Publication Year: "))
    genre = input("Genre: ").strip()
    read_input = input("Have you read this book? (y/n): ").strip().lower()
    read = True if read_input == 'y' else False

    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }
    library.append(book)
    print(f"✅ '{title}' has been added to your library.")

# Function to remove a book
def remove_book():
    print("\n❌ Remove a Book")
    title = input("Enter the title of the book to remove: ").strip()
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print(f"✅ '{title}' has been removed from your library.")
            return
    print("⚠️ Book not found.")

# Function to search for books
def search_book():
    print("\n🔍 Search for a Book")
    keyword = input("Enter title or author to search: ").strip().lower()
    results = [book for book in library if keyword in book["title"].lower() or keyword in book["author"].lower()]
    
    if results:
        print(f"\n🔎 Found {len(results)} matching book(s):")
        display_books(results)
    else:
        print("⚠️ No matching books found.")

# Function to display all books
def display_books(books=None):
    if books is None:
        books = library

    if not books:
        print("📭 No books in the library.")
        return

    print("\n📚 Your Book Library:")
    for idx, book in enumerate(books, 1):
        read_status = "Read" if book["read"] else "Unread"
        print(f"{idx}. '{book['title']}' by {book['author']} ({book['year']}) - {book['genre']} [{read_status}]")

# Function to display stats
def display_stats():
    total = len(library)
    read_count = sum(1 for book in library if book["read"])
    read_percentage = (read_count / total * 100) if total > 0 else 0
    print("\n📊 Library Statistics:")
    print(f"Total books: {total}")
    print(f"Books read: {read_count} ({read_percentage:.2f}%)")

# Menu system
def main_menu():
    while True:
        print("\n=== 📖 Book Library Menu ===")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            add_book()
        elif choice == '2':
            remove_book()
        elif choice == '3':
            search_book()
        elif choice == '4':
            display_books()
        elif choice == '5':
            display_stats()
        elif choice == '6':
            print("👋 Goodbye! Exiting the program.")
            break
        else:
            print("⚠️ Invalid choice. Please enter a number between 1 and 6.")

# Run the program
if __name__ == "__main__":
    main_menu()
