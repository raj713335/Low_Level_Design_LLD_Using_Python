class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        print(f"Books in {self.name}:")
        for book in self.books:
            print(f" - {book.title}")


class Book:
    def __init__(self, title, library):
        self.title = title
        self.library = library

    def show_library(self):
        print(f"{self.title} is in {self.library.name}")


if __name__ == "__main__":
    library = Library("City Library")

    book1 = Book("1984", library)
    book2 = Book("Brave New World", library)

    library.add_book(book1)
    library.add_book(book2)

    library.show_books()
    book1.show_library()
    book2.show_library()
