'''
Assignment 5: Shopping Bill Calculator

A retail shop wants to calculate the total bill for a customer.

Create a class ShoppingBill with the following attributes:
- Product name
- Product price
- Quantity
- Discount percentage
- GST percentage

Create the following methods:
- calculate_subtotal() – Calculate price × quantity.
- calculate_discount() – Calculate the discount amount.
- calculate_gst() – Calculate GST on the discounted amount.
- calculate_final_bill() – Calculate the final payable amount.
- display_bill() – Display the complete bill details.

Formula:

Subtotal = Price × Quantity
Discounted Amount = Subtotal - Discount
GST = Discounted Amount × GST Percentage / 100
Final Bill = Discounted Amount + GST
'''
class Bill:

    def __init__(self,pName,pPrice,pQuantity,discount,gstPercent):
        self.pName=pName
        self.pPrice=pPrice
        self.pQuantity=pQuantity
        self.discount=discount
        self.gstPercent=gstPercent

    def calc_subTotal(self):
        return self.pPrice*self.pQuantity
    
    def calc_discount(self):
        return self.calc_subTotal()-(self.calc_subTotal()*self.discount/100)
    
    def calc_gst(self):
        return self.calc_discount()*self.gstPercent/100
    
    def calc_final(self):
        return self.calc_discount()+self.calc_gst()
    
    def display(self):
        print(f"Product Name: {self.pName}")
        print(f"Product Price: {self.pPrice}")
        print(f"Quantity: {self.pQuantity}")
        print(f"Discount Percentage: {self.discount}%")
        print(f"GST Percentage: {self.gstPercent}%")
        print(f"Subtotal: {self.calc_subTotal()}")
        print(f"Discounted Amount: {self.calc_discount()}")
        print(f"GST: {self.calc_gst()}")
        print(f"Final Bill: {self.calc_final()}")


    
b1 = Bill("Laptop", 50000, 2, 10, 18)
b1.display()