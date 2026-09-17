'''
Question 3: Online Shopping System
Scenario

An e-commerce company wants to calculate the final amount payable by customers after applying discounts.

Requirements

Create a class named Product with:

product_id
product_name
quantity
price_per_item

Initialize the values using a constructor.

Calculations
Total Amount = Quantity × Price Per Item
If Total Amount > ₹5000, Discount = 10%
Otherwise, Discount = 5%
Final Amount = Total Amount − Discount
Sample Input
Enter Product ID : P101
Enter Product Name : Laptop
Enter Quantity : 2
Enter Price Per Item : 35000
Sample Output
------ Shopping Bill ------
Product ID        : P101
Product Name      : Laptop
Quantity          : 2
Price Per Item    : 35000.0
Total Amount      : ₹70000.0
Discount          : ₹7000.0
Final Amount      : ₹63000.0
'''

class bill:

    def __init__(self,pId,pName,pQuantity,pricePerItems):
        self.pId=pId
        self.pName=pName
        self.pQuantity=pQuantity
        self.pricePerItems=pricePerItems
    
    def totalAmt(self):
        totalAmt=self.pQuantity*self.pricePerItems
        return totalAmt
    def discount(self):
        if self.totalAmt()>5000:
            return self.totalAmt()/10
        else:
            return self.totalAmt()/20
    def finalAmt(self):
        return self.totalAmt()-self.discount()
    

    def display(self):
        print("------ Shopping Bill ------")
        print("Product ID        :", self.pId)
        print("Product Name      :", self.pName)
        print("Quantity          :", self.pQuantity)
        print("Price Per Item    :", float(self.pricePerItems))
        print("Total Amount      : ₹", self.totalAmt())
        print("Discount          : ₹", self.discount())
        print("Final Amount      : ₹", self.finalAmt())
        

product = bill("P101", "Laptop", 2, 35000)
product.display()