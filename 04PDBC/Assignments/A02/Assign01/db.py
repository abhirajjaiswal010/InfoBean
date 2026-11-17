import mysql.connector as db


def get_connection():
    con = db.connect(
        host="localhost",
        user="root",
        password="sql@123",
        database="OnlineShoppingDB",
        autocommit=True,
    )
    return con


con = get_connection()

if con.is_connected():
    print("DB Connect SuccessFully")
    cur = con.cursor()

    # insert data
    customer_query = """
insert ignore into customer_order_pdbc
values (%s,%s,%s,%s)
 """
    customers = [
        (1, "Amit", "Indore", "amit@gmail.com"),
        (2, "Priya", "Bhopal", "priya@gmail.com"),
        (3, "Rahul", "Indore", "rahul@gmail.com"),
        (4, "Neha", "Ujjain", "neha@gmail.com"),
        (5, "Karan", "Dewas", "karan@gmail.com"),
    ]

    product_query='''
insert ignore into product_order_pdbc
values (%s,%s,%s,%s,%s)
'''
    products=[(101, "Laptop", "Electronics", 55000, 10),
        (102, "Mouse", "Electronics", 800, 50),
        (103, "Keyboard", "Electronics", 1500, 30),
        (104, "Notebook", "Stationery", 100, 100),
        (105, "Monitor", "Electronics", 12000, 15),
        (106, "Pen", "Stationery", 20, 200)]
    
    order_query='''
insert ignore into customer_order_details
values (%s,%s,%s,%s,%s)
'''
    
    orders = [
        (1001, 1, 101, 1, "Delivered"),
        (1002, 1, 102, 2, "Delivered"),
        (1003, 2, 103, 1, "Shipped"),
        (1004, 3, 105, 2, "Delivered"),
        (1005, 3, 104, 5, "Pending"),
        (1006, 4, 101, 1, "Pending"),
        (1007, 5, 106, 10, "Delivered")
    ]

    cur.executemany(customer_query,customers)
    cur.executemany(product_query,products)
    cur.executemany(order_query,orders)

    print("Initial Data Insert SuccessFully")

    cur.close()
    con.close()
else:
    print("DB Failed To Connect")
