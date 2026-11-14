import mysql.connector as db


def get_connection():

    con = db.connect(
        host="localhost",
        user="root",
        password="sql@123",
        database="pdbcAssign03",
        autocommit=True,
    )

    return con


con = get_connection()

if con.is_connected():
    print("DB is connected successfully")

    cur = con.cursor()

    query = """
        CREATE TABLE IF NOT EXISTS product_pdbc (
            pid INT PRIMARY KEY,
            pname VARCHAR(50),
            category VARCHAR(50),
            price DECIMAL(10,2),
            quantity int
        )
    """

    cur.execute(query)

    InsertQuery = """
        INSERT ignore INTO product_pdbc (pid, pname, category, price, quantity)
        VALUES (%s, %s, %s, %s, %s)
    """

    products = [
        (301, "Laptop", "Electronics", 55000.00, 10),
        (302, "Mouse", "Electronics", 800.00, 50),
        (303, "Keyboard", "Electronics", 1500.00, 30),
        (304, "Notebook", "Stationery", 100.00, 100),
        (305, "Pen", "Stationery", 20.00, 200),
    ]

    cur.executemany(InsertQuery, products)

    print(cur.rowcount, "Products inserted successfully")

    cur.close()
    con.close()

else:
    print("DB is not connected")
