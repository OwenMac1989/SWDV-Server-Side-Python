from objects import Book, Author, Authors

def main():
    print("The Authors Tester program")
    print()
    
    author1 = Author("Mark", "Twain")
    author2 = Author("Charles", "Warner")
    authors = Authors()
    authors.add(author1)
    authors.add(author2)
    book = Book("The Gilded Age", authors)

    # display the book data
    print("BOOK DATA - SINGLE LINE")
    print(book)
    print()

    print("BOOK DATA - MUTLIPLE LINES")
    print("Title:   ", book.title)
    if book.authors.count > 1:
        print("Authors: ",  book.authors)
    else:
        print("Author: ",  book.authors)
    
    print()
    print("Authors: ")
    for a in authors:
        print(f"{a}")
        
if __name__ == "__main__":
    main()
