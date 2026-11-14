
from product_operation import (
    add_product,
    display_products,
    search_product,
    update_price,
    delete_product
)


while True:

    print("PRODUCT MANAGEMENT SYSTEM")
    print("1. Add Product")
    print("2. Display All Products")
    print("3. Search Product by Name")
    print("4. Update Product Price")
    print("5. Delete Product")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_product()

    elif choice == 2:
        display_products()

    elif choice == 3:
        search_product()

    elif choice == 4:
        update_price()

    elif choice == 5:
        delete_product()

    elif choice == 6:
        print("Thank you for using Product Management System.")
        break

    else:
        print("Invalid choice! Please enter a valid choice.")
