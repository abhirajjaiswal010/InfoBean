class Book:

    def __init__(self,book_id,book_name,author,price):
        self.book_id=book_id
        self.book_name=book_name
        self.author=author
        self.price=price

    def display(self):
        print(f"{self.book_id} {self.book_name} {self.author} {self.price}")

    def search(self,id):
        return self.book_id==id
    
    def sort_by_author(self,author):
        return self.author==author
    
    def price_greater_100(self):
        return self.price>100
    
    def expensive(self,other):
        return self.price>other.price
    
    def avg(self,book):
        total=0
        for b in book:
            total+=self.price
        
        return total/len(book)
