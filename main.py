import sqlite3

def main():
    conn = sqlite3.connect("my_database.db")
    cursor = conn.cursor()
    # Drop tables
    # Drop tables
    cursor.execute("DROP TABLE IF EXISTS customers;")
    cursor.execute("DROP TABLE IF EXISTS orders;")
    cursor.execute("DROP TABLE IF EXISTS order_items;")
    cursor.execute("DROP TABLE IF EXISTS products;")
    
    # Create tables
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS customers (
            customer_id INT PRIMARY KEY,
            customer_name VARCHAR(255)
        );"""
    )

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS orders (
            order_id INT PRIMARY KEY,
            order_date DATE,
            customer_id INT,
            FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
        );"""
    )

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS order_items (
            order_item_id INT PRIMARY KEY,
            order_id INT,
            product_id INT,
            quantity INT,
            unit_price DECIMAL(10, 1),
            FOREIGN KEY (order_id) REFERENCES orders(order_id),
            FOREIGN KEY (product_id) REFERENCES products(product_id)
        );"""
    )

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS products (
            product_id INT PRIMARY KEY,
            product_name VARCHAR(255)
        );"""
    )

    

    # Insert data
    cursor.execute(
        """INSERT INTO customers (customer_id, customer_name)
            VALUES
                (1, 'Customer A'),
                (2, 'Customer B'),
                (3, 'Customer C'),
                (4, 'Customer D');
        """
    )

    cursor.execute(
        """INSERT INTO orders (order_id, order_date, customer_id)
            VALUES
                (1, '2023-10-01', 1),
                (2, '2023-10-02', 2),
                (3, '2023-10-03', 3),
                (4, '2023-10-04', 4);
        """
    )

    cursor.execute(
        """INSERT INTO order_items (order_item_id, order_id, product_id, quantity, unit_price)
            VALUES
                (1, 1, 1, 1, 1.0),
                (2, 2, 2, 2, 2.0),
                (3, 3, 3, 3, 3.0),
                (4, 4, 4, 4, 4.0),
                (5, 1, 2, 2, 2.0);
        """
    )

    cursor.execute(
        """INSERT INTO products (product_id, product_name)
            VALUES
                (1, 'P1'),
                (2, 'P2'),
                (3, 'P3'),
                (4, 'P4');
        """
    )

    # Commit the changes
    conn.commit()

    # Query data
    cursor.execute(
        """
    SELECT
        c.customer_id,
        c.customer_name,
        SUM(oi.quantity * oi.unit_price) AS total_revenue
    FROM
        customers c
    JOIN
        orders o ON c.customer_id = o.customer_id
    JOIN
        order_items oi ON oi.order_id = o.order_id
    GROUP BY 
        c.customer_id
    ORDER BY
        total_revenue DESC;
    """
    )
    
    rows = cursor.fetchall()
    print("**********print results************")
    for row in rows:
        print(row)


main()
