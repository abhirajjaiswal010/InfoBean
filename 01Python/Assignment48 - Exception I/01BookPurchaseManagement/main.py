from model.book import Book, InvalidQuantityException

print("FOR OWNER OF STORE\n")

book_id = input("Enter Book Id : ")
book_title = input("Enter Book Title : ")
author_name = input("Enter Author Name : ")
price = int(input("Enter Price : "))
quantity = int(input("Enter Book Quantity : "))

b1 = Book(book_id, book_title, author_name, price, quantity)

print("\nBook Details\n")
b1.display()

print("\nFOR CUSTOMER\n")

customer_quantity = int(input("Enter Quantity For Buy : "))

try:
    b1.purchase(customer_quantity)

except InvalidQuantityException as e:
    print(f"\n{e}")