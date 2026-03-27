-- Esquema de exemplo para praticar

CREATE TABLE customers (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(150)
);

CREATE TABLE orders (
  id INT AUTO_INCREMENT PRIMARY KEY,
  customer_id INT,
  order_date DATE,
  FOREIGN KEY (customer_id) REFERENCES customers(id)
);

CREATE TABLE order_items (
  id INT AUTO_INCREMENT PRIMARY KEY,
  order_id INT,
  product_name VARCHAR(150),
  quantity INT,
  unit_price DECIMAL(10,2),
  FOREIGN KEY (order_id) REFERENCES orders(id)
);

-- Inserir dados de exemplo
INSERT INTO customers (name, email) VALUES ('Alice','alice@example.com'), ('Bob','bob@example.com');

INSERT INTO orders (customer_id, order_date) VALUES (1, DATE_SUB(CURDATE(), INTERVAL 2 MONTH)), (2, DATE_SUB(CURDATE(), INTERVAL 1 MONTH));

INSERT INTO order_items (order_id, product_name, quantity, unit_price) VALUES (1,'Produto A',2,50.00),(1,'Produto B',1,150.00),(2,'Produto A',3,50.00);
