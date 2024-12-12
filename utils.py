import MySQLdb

def connect():

    try:
        conn = MySQLdb.connect(
            db ='pcrud',
            host = 'localhost',
            user = 'root',
            passwd = 'admin123'
        )
        return conn
    except MySQLdb.Error as e:
        print(f'Error connecting to MySQL Server: {e}')

def disconnect(conn):

    if conn:
        conn.close()

def listproducts():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()

    if len(products) > 0:
        print('List products')
        print('-------------')
        for product in products:
            print(f'ID: {product[0]}')
            print(f'Name: {product[1]}')
            print(f'Price: {product[2]}')
            print(f'Stock: {product[3]}')
    else:
        print("Don't have products in register.")

def insert():
    conn = connect()
    cursor = conn.cursor()

    name = input('Enter the product name: ')
    price = float(input('Enter the product price: '))
    stock = int(input('Enter the quantity in stock: '))

    sql = "INSERT INTO products (name, price, stock) VALUES (%s, %s, %s)"
    val = (name, price, stock)
    cursor.execute(sql, val)
    conn.commit()

    if cursor.rowcount == 1:
        print(f"The product {name} was inserted successfully.")
    else:
        print("The product could not be inserted.")

    disconnect(conn)

def update():
    conn = connect()
    cursor = conn.cursor()

    code = int(input('Enter the product code: '))
    name = input('Enter the new product name: ')
    price = float(input('Enter the new product price: '))
    stock = int(input('Enter the new stock quantity: '))

    cursor.execute(f"UPDATE products SET name='{name}', price={price}, stock={stock} WHERE id={code}")
    conn.commit()

    if cursor.rowcount == 1:
        print(f'The product {name} was successfully updated.')
    else:
        print('Error updating the product.')

    disconnect(conn)


def delete():
    conn = connect()
    cursor = conn.cursor()

    code = int(input('Enter the product code: '))

    cursor.execute(f'DELETE FROM products WHERE id={code}')
    conn.commit()

    if cursor.rowcount == 1:
        print('Product successfully deleted.')
    else:
        print(f'Error deleting the product with id = {code}')

    disconnect(conn)


def menu():
    print('==========Management of Products==============')
    print('Select an option: ')
    print('1 - List products.')
    print('2 - Insert products.')
    print('3 - Update product.')
    print('4 - Delete product.')
    option = int(input())
    if option in [1, 2, 3, 4]:
        if option == 1:
            listproducts()
        elif option == 2:
            insert()
        elif option == 3:
            update()
        elif option == 4:
            delete()
    else:
        print('Invalid option')