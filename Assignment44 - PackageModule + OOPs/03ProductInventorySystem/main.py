from models.product import Product

print("-" * 20)
print("Product Inventory System")
print("-" * 20)

productDB=[]


for i in range(3):
    print()

    print(f"Enter {i+1}th Product")
    id=int(input("Enter Product ID :"))
    name=input("Enter Product Name : ")
    price=int(input("Enter Product Price : "))
    quantity=int(input("Enter Product Quantity : "))
    print()
    p=Product(id,name,price,quantity)
    productDB.append(p)


print("-" * 20)
print("All Product List")
print("-" * 20)

for p in productDB:
    p.display()

print("-" * 20)
print("Total Value Of Each")
print("-" * 20)

for p in productDB:
    p.total_value()


print("-" * 20)
print("Product Stock <10")
print("-" * 20)

for p in productDB:
    if p.quantity_lessthan10():
        p.display()

print("-" * 20)
print("Highest Price")
print("-" * 20)

high=productDB[0]

for p in productDB:
    if p.highest(high):
        high=p

high.display()

print("-" * 20)
print("Total Inventory")
print("-" * 20)

total=0

for p in productDB:
    total=p.total_inventory(total)

print(total)


print("-" * 20)
print("Search Product ..")
print("-" * 20)

search_id=int(input("Enter ID Of Product : "))

for p in productDB:
    if p.search(search_id):
        p.display()
        print("Item Found")
        break
else:
    print("item not Found")

