import sorts
import utils

bookshelf = utils.load_books("books_small.csv")
long_bookshelf = utils.load_books("books_large.csv")

def by_title_ascending(book_a, book_b):
    if book_a["title_lower"] > book_b["title_lower"]:
        return True
    else:
        return False

def by_author_ascending(book_a, book_b):
    if book_a["author_lower"] > book_b["author_lower"]:
        return True
    else:
        return False

def by_total_length(book_a, book_b):
    if len(book_a["title_lower"]) + len(book_a["author_lower"]) > len(book_b["title_lower"]) + len(book_b["author_lower"]):
        return True
    else:
        return False

bookshelf_copy = bookshelf.copy()
bookshelf_copy_2 = bookshelf.copy()
long_bookshelf_copy = long_bookshelf.copy()

sort_1 = sorts.bubble_sort(bookshelf, by_title_ascending)
for book in sort_1:
    print(book["title"])

sort_2 = sorts.bubble_sort(bookshelf_copy, by_author_ascending)
for book in sort_2:
    print(book["author"])

sorts.quicksort(bookshelf_copy_2, 0, len(bookshelf_copy_2) - 1, by_author_ascending)
for book in bookshelf_copy_2:
    print(book["author"])

bubble_sort_long = sorts.bubble_sort(long_bookshelf, by_total_length)
for book in bubble_sort_long:
    print(str(book["title"]) + ":", book["author"])

sorts.quicksort(long_bookshelf_copy, 0, len(long_bookshelf_copy) - 1, by_total_length)
for book in long_bookshelf_copy:
    print(str(book["title"]) + ":", book["author"])