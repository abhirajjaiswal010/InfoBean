
from database import get_connection


def add_product():

    con = get_connection()
    cur = con.cursor()

    pid = int(input("Enter Product ID: "))
    pname = input("Enter Product Name: ")
    category = input("Enter Category: ")
    price = float(input("Enter Price: "))
    quantity = int(input("Enter Quantity: "))

    query = """
        INSERT INTO product_pdbc
        (pid, pname, category, price, quantity)
        VALUES (%s, %s, %s, %s, %s)
    """

    values = (pid, pname, category, price, quantity)

    cur.execute(query, values)

    print("Product inserted successfully.")

    cur.close()
    con.close()


def display_products():

    con = get_connection()
    cur = con.cursor()

    query = "SELECT * FROM product_pdbc"

    cur.execute(query)

    products = cur.fetchall()

    if products:

        for product in products:
            print(product)

    else:
        print("No product records found.")

    cur.close()
    con.close()


def search_product():

    con = get_connection()
    cur = con.cursor()

    search_name = input("Enter product name to search: ")

    query = """
        SELECT * FROM product_pdbc
        WHERE pname LIKE %s
    """

    cur.execute(query, ('%' + search_name + '%',))

    products = cur.fetchall()

    if products:

        for product in products:
            print(product)

    else:
        print("No matching products found.")

    cur.close()
    con.close()


def update_price():

    con = get_connection()
    cur = con.cursor()

    pid = int(input("Enter Product ID: "))
    price = float(input("Enter New Price: "))

    query = """
        UPDATE product_pdbc
        SET price = %s
        WHERE pid = %s
    """

    cur.execute(query, (price, pid))

    if cur.rowcount > 0:
        print("Product price updated successfully.")
    else:
        print("Product not found or price unchanged.")

    cur.close()
    con.close()


def delete_product():

    con = get_connection()
    cur = con.cursor()

    pid = int(input("Enter Product ID: "))

    query = """
        DELETE FROM product_pdbc
        WHERE pid = %s
    """

    cur.execute(query, (pid,))

    if cur.rowcount > 0:
        print("Product deleted successfully.")
    else:
        print("Product not found.")

    cur.close()
    con.close()
