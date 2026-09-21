from models.book import Book

print("-" * 20)
print("BOOK MANAGEMENT SYSTEM")
print("-" * 20)

bookDB = []



print("--- Enter Book Details ---")

for i in range(3):

    print(f"Book {i + 1}")

    book_id = int(input("Enter Book ID : "))
    book_name = input("Enter Book Name : ")
    author = input("Enter Author : ")
    price = int(input("Enter Price : "))

    book = Book(book_id, book_name, author, price)
    bookDB.append(book)




print("-" * 20)
print("ALL BOOKS")
print("-" * 20)

for b in bookDB:
    b.display()




print("-" * 20)
print("SEARCH BOOK")
print("-" * 20)

id = int(input("Enter Book ID : "))

for b in bookDB:
    if b.search(id):
        b.display()




print("-" * 20)
print("SEARCH BY AUTHOR")
print("-" * 20)

author = input("Enter Author : ")

for b in bookDB:
    if b.sort_by_author(author):
        b.display()




print("-" * 20)
print("PRICE GREATER THAN 100")
print("-" * 20)

for b in bookDB:
    if b.price_greater_100():
        b.display()




print("-" * 20)
print("MOST EXPENSIVE BOOK")
print("-" * 20)

high = bookDB[0]

for b in bookDB:
    if b.expensive(high):
        high = b

high.display()




print("-" * 20)
print("AVERAGE PRICE")
print("-" * 20)

a=bookDB[0].avg(bookDB)
print(f"{a:.2f}")