'''
Q1. BOOK PURCHASE MANAGEMENT

Mohan is a librarian and wants to develop a small Python application to manage
book purchases. The system should ensure that a customer cannot purchase more
books than the quantity currently available.

Create a class named Book with the following attributes:

1. book_id       - String
2. book_title   - String
3. author_name  - String
4. price        - float
5. quantity     - int

Create a custom exception class named:

InvalidQuantityException

Requirements:

1. Create the Book class with the above attributes.

2. Create a custom exception InvalidQuantityException by inheriting from
   the built-in Exception class.

3. Create a method purchase(quantity).

4. If the requested purchase quantity is greater than the available quantity,
   raise InvalidQuantityException with the message:

   Quantity not available

5. If the purchase is successful, reduce the available quantity.

6. Display the remaining quantity.

7. Use try-except to handle the custom exception.

8. Quantity purchased must be a positive integer.

## Input:

Enter Book ID:
YCW2019

Enter Book Title:
You can win

Enter Author Name:
Shiv Khera

Enter Price:
245

Enter Available Quantity:
25

Enter Quantity to Purchase:
20

## Output:

Quantity Available : 5

## Test Case 2:

Input:
Book ID       : YCW2019
Book Title    : You can win
Author Name   : Shiv Khera
Price         : 245
Available Qty : 25
Purchase Qty  : 30

## Output:

InvalidQuantityException: Quantity not available
'''

