

from operation import (
    addCustomer,
    addProduct,
    placeOrder,
    displayAll,
    searchCustomer,
    updateOrderStatus,
    updateProductPrice,
    deleteOrder,
    displayCustomerWise,
    displayProductCost,
    displayCustomerNotPlaceOrder,
    displayCustomer
)


while True:

        print("\n========== ONLINE SHOPPING MANAGEMENT SYSTEM ==========")

        print("""
        1.  Add Customer
        2.  Add Product
        3.  Place Order
        4.  Display All Orders
        5.  Search Customer
        6.  Update Product Price
        7.  Update Order Status
        8.  Delete Order
        9.  Display Customer-wise Total Purchase
        10. Display Products Costing More Than Average
        11. Display Customers Who Have Not Placed Orders
        12. Display Customers Who Have Placed Orders
        13.  Exit
        """)

        
        choice = int(input("Enter Your Choice: "))

        match choice:

            case 1:
                addCustomer()

            case 2:
                addProduct()

            case 3:
                placeOrder()

            case 4:
                displayAll()

            case 5:
                searchCustomer()

            case 6:
                updateProductPrice()

            case 7:
                updateOrderStatus()

            case 8:
                deleteOrder()

            case 9:
                displayCustomerWise()

            case 10:
                displayProductCost()

            case 11:
                displayCustomerNotPlaceOrder()

            case 12:
                displayCustomer()

            case 13:
                print("Thank You! Exiting Application...")
                break

            case _:
                print("Invalid Choice! Please Select 0-12.")


