import csv

def load_books(filename):
    bookshelf = []

    with open(filename) as file:
        shelf = csv.DictReader(file)
        for book in shelf:
            bookshelf.append(book)
    return bookshelf