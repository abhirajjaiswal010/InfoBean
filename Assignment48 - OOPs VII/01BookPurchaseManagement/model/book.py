class Book:
    def __init__(self, book_id, book_title, author_name, price, quantity):
        self.book_id = book_id
        self.book_title = book_title
        self.author_name = author_name
        self.price = price
        self.quantity = quantity
    
    def display(self):
        print("Book ID:", self.book_id)
        print("Book Title:", self.book_title)
        print("Author Name:", self.author_name)
        print("Price:", self.price)
        print("Quantity:", self.quantity)

    def purchase(self, quantity):
        if quantity > self.quantity:
            raise InvalidQuantityException("Qauntity not available")

        self.quantity -= quantity
        print(f"Remaining Quantity : {self.quantity}")


class InvalidQuantityException(Exception):
    pass
