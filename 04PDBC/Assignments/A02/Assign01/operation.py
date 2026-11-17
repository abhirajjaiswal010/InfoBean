from db import get_connection
from tabulate import tabulate

def addCustomer():


    con=get_connection()
    cur=con.cursor()

    id=int(input("Enter Id : "))
    name=input("Enter Name : ")
    city=input("Enter City :")
    email=input("Enter Email :")

    query='''
insert into customer_order_pdbc
values (%s,%s,%s,%s)
'''
    values=(id,name,city,email)

    cur.execute(query,values)

    print("Customer Added Successfully")

    cur.close()
    con.close()


    
def addProduct():
    con=get_connection()
    cur=con.cursor()

    id=int(input("Enter Id:"))
    name=input("Enter Product Name :")
    category=input("Enter Category :")
    price=int(input("Enter Price :"))
    stock=int(input("Enter Stock:"))

    query='''
insert into product_order_pdbc
values(%s,%s,%s,%s,%s)
'''
    values=(id,name,category,price,stock)

    cur.execute(query,values)

    print("Product Added Successfully")

    cur.close()
    con.close()


def placeOrder():
    con=get_connection()
    cur=con.cursor()

    OrderId=int(input("Enter Order Id : "))
    CustomerId=int(input("Enter Customer Id :"))
    ProductId=int(input("Enter Product Id :"))
    quantity=int(input("Enter quantity :"))
    status=int(input("Enter Status :"))

    query='''
insert into customer_order_details
values (%s,%s,%s,%s,%s)
'''
    values=(OrderId,CustomerId,ProductId,quantity,status)

    cur.execute(query,values)
    print("Order Placed Successfully")

    cur.close()
    con.close()


def displayAll():

    con=get_connection()
    cur=con.cursor()

    query = """
        SELECT
            o.order_id,
            c.customer_name,
            p.product_name,
            o.quantity,
            p.price,
            (o.quantity * p.price) AS calculate_amt,
            o.order_status

        FROM customer_order_pdbc c

        JOIN customer_order_details o
            ON c.customer_id = o.customer_id

        JOIN product_order_pdbc p
            ON p.product_id = o.product_id;
    """
    cur.execute(query)

    records=cur.fetchall()

    # for r in records:
    #     print(r)
    headers = [
    "Order ID",
    "Customer",
    "Product",
    "Quantity",
    "Price",
    "Amount",
    "Status"
]

    print(tabulate(records, headers=headers, tablefmt="rounded_grid"))

    print(f"{cur.rowcount} Display Successfully")

    cur.close()
    con.close()


def searchCustomer():
    
    con=get_connection()
    cur=con.cursor()

    name=input("Enter Name : ")


    query='''
select * from customer_order_pdbc
where customer_name like %s
'''
    cur.execute(query,('%'+name+'%',))
    records=cur.fetchall()

    if records:
        header=[
            "customer_id",
            "customer_name",
            "city",
            "email"
        ]

        print(tabulate(records,headers=header,tablefmt="rounded_grid"))
        print(f"{cur.rowcount} Record Found For name {name}")

    else:
        print("Record Not Found")

    cur.close()
    con.close()


def updateProductPrice():
    con=get_connection()
    cur=con.cursor()

    id=input("Enter Id:")
    price=int(input("Enter New Price : "))

    query='''
update product_order_pdbc
set price=%s
where id=%s
'''
    values=(price,id)

    cur.execute(query,values)

    if cur.rowcount>0:
        print("Product Price Update SuccessFully")
    else:
        print("Product Price Update Fail")
    
    cur.close()
    con.close()

def updateOrderStatus():
    con=get_connection()
    cur=con.cursor()

    id=input("Enter Id:")
    print("""
    Select Order Status:
    1. Pending
    2. Shipped
    3. Delivered
    """)

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        status = "Pending"
    elif choice == 2:
        status = "Shipped"
    elif choice == 3:
        status = "Delivered"
    else:
        print("Invalid Choice!")
        return
    
    query='''
update customer_order_details
set order_status=%s
where id=%s

'''
    values=(status,id)

    cur.execute(query,values)

    if cur.rowcount>0:
        print("Status Update Success")
    else:
        print("Status Update Failed")
    
    cur.close()
    con.close()

def deleteOrder():
    con=get_connection()
    cur=con.cursor()

    id=int(input("Enter ID : "))

    query='''
delete from customer_order_details  
where order_id=%s
'''
    cur.execute(query,(id,))

    if cur.rowcount>0:
        print("Delete Success")
    else:
        print("Delete Failed")

    cur.close()
    con.close()


def displayCustomerWise():
    con=get_connection()
    cur=con.cursor()

    query='''
select c.customer_id,c.customer_name,sum(o.quantity*p.price) as total_purchase_amount
from customer_order_pdbc c
join customer_order_details o
on c.customer_id=o.customer_id
join product_order_pdbc p
on o.product_id=p.product_id
group by c.customer_id;

'''

    cur.execute(query)
    record=cur.fetchall()

    header=[
        "Customer_id",
        "Customer_Name",
        "Total_Purchase_Amount"
    ]

    print(tabulate(record,headers=header,tablefmt="rounded_grid"))

    cur.close()
    con.close()

def displayProductCost():
    con=get_connection()
    cur=con.cursor()
    query='''

select product_id,product_name,price
from product_order_pdbc
where price>(
select avg(price)
from product_order_pdbc

)


'''
    cur.execute(query)
    record=cur.fetchall()

    header=["product_id","product_name","price"]
    print(tabulate(record,headers=header,tablefmt="rounded_grid"))

    cur.close()
    con.close()

def displayCustomer():
    con=get_connection()
    cur=con.cursor()
    query='''
SELECT customer_id, customer_name
FROM customer_order_pdbc
WHERE customer_id IN (
    SELECT customer_id
    FROM customer_order_details
)

'''

    cur.execute(query)
    record=cur.fetchall()
    header=["customer_id","customer_name"]
    print(tabulate(record,headers=header,tablefmt="rounded_grid"))

    cur.close()
    con.close()


def displayCustomerNotPlaceOrder():
    con=get_connection()
    cur=con.cursor()

    query='''
SELECT customer_id, customer_name
FROM customer_order_pdbc
WHERE customer_id not IN (
    SELECT customer_id
    FROM customer_order_details
)
'''
    cur.execute(query)
    record=cur.fetchall()
    header=["customer_id","customer_name"]
    print(tabulate(record,headers=header,tablefmt="rounded_grid"))

    cur.close()
    con.close()


    











