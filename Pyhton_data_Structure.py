def add_book(library, title, author):
    new_book = (title, author)
    if new_book not in library:
        library.append(new_book)
        print(f"Book '{title}' by {author} added to the library.")
    else:
        print("This book already exists in the library.")

# current books in library
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

# adding new books to the library
add_book(library, "The Great Gatsby", "F Scott. Fitzgerald")
add_book(library, "Harry Potter", "J.K. Rowling")

print("Updated Library:", library)
