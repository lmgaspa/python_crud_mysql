# Product Management System

A simple Python-based Product Management System that performs CRUD (Create, Read, Update, Delete) operations on a MySQL database.

## Features

- **List Products**: Retrieve and display all products stored in the database.
- **Insert Products**: Add a new product with details like name, price, and stock quantity.
- **Update Products**: Modify existing product details based on the product ID.
- **Delete Products**: Remove a product from the database by specifying its ID.

## Requirements

- Python 3.x
- MySQL server
- MySQLdb library (`pip install mysqlclient`)

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/product-management-system.git
    cd product-management-system
    ```

2. Install required dependencies:
    ```bash
    pip install mysqlclient
    ```

3. Set up a MySQL database:
    - Create a database named `pcrud` and a table named `products`:
      ```sql
      CREATE DATABASE pcrud;
      USE pcrud;
      CREATE TABLE products (
          id INT AUTO_INCREMENT PRIMARY KEY,
          name VARCHAR(255),
          price FLOAT,
          stock INT
      );
      ```
    - Replace the `host`, `user`, and `passwd` values in the `connect()` function with your MySQL server credentials.

## Usage

1. Run the script:
    ```bash
    python main.py
    ```

2. Select an option from the menu to perform a specific operation:
    ```
    ==========Management of Products==============
    Select an option:
    1 - List products.
    2 - Insert products.
    3 - Update product.
    4 - Delete product.
    ```

3. Follow the prompts to manage your products.

## Code Structure

### Functions

- **`connect()`**: Establish a connection to the MySQL database.
- **`disconnect(conn)`**: Close the database connection.
- **`listproducts()`**: Fetch and display all products.
- **`insert()`**: Add a new product to the database.
- **`update()`**: Update an existing product's details.
- **`delete()`**: Remove a product from the database.
- **`menu()`**: Display the menu and call the corresponding functions.

### Example Workflow

1. **List Products**:
    ```
    ID: 1
    Name: Laptop
    Price: 1200.99
    Stock: 10
    ```

2. **Insert a Product**:
    ```
    Enter the product name: Mouse
    Enter the product price: 25.99
    Enter the quantity in stock: 50
    The product Mouse was inserted successfully.
    ```

3. **Update a Product**:
    ```
    Enter the product code: 1
    Enter the new product name: Gaming Laptop
    Enter the new product price: 1500.99
    Enter the new stock quantity: 5
    The product Gaming Laptop was successfully updated.
    ```

4. **Delete a Product**:
    ```
    Enter the product code: 2
    Product successfully deleted.
    ```

## Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.
