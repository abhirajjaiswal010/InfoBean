from pathlib import Path as path
from rich.prompt import Prompt

base_dir = path(__file__).parent
file_path = base_dir / "shop.txt"

n = int(input("Enter number of orders: "))

with open(file_path, "w+") as f:
    for i in range(n):
        print(f"\n Order {i + 1}th Info\n")

        order_id = int(input("Enter Order Id  :"))
        name = input("Enter Customer Name :")
        product = input("Enter Product    :")
        quantity = int(input("Enter Quantity  :"))
        price = int(input("Enter Price        :"))
        f.write(f"{order_id} {name} {product} {quantity} {price}\n")

    f.seek(0)

    products = f.readlines()

    total_amt = 0
    highest_order = float("-inf")
    highest_order_id = 0
    highest_order_name = ""

    for i in products:
        order_id, name, product, quantity, price = i.split()

        total_amt = int(quantity) * int(price)
        print(f"{order_id} {name} {product} " 
              f" Quantity:{quantity} Total:{total_amt}")

        if total_amt > highest_order:
            highest_order = total_amt
            highest_order_id = order_id
            highest_order_name = name

    print("\n Highest Order \n")

    print(f"Order Id  : {highest_order_id}")
    print(f"Customer Name  : {highest_order_name}")
    print(f"Total Amount : {highest_order}")
