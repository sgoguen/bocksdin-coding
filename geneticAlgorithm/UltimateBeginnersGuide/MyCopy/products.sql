CREATE DATABASE products;
CREATE TABLE products (
  product_id INT NOT NULL AUTO_INCREMENT,
  product_name VARCHAR(50) NOT NULL,
  space FLOAT NOT NULL,
  price FLOAT NOT NULL,
  quantity INT NOT NULL,
  CONSTRAINT pk_products_product_id PRIMARY KEY (product_id)
);


INSERT INTO products (product_name, space, price, quantity) VALUES ('Refrigerator A', 0.751, 999.90, 1);
INSERT INTO products (product_name, space, price, quantity) VALUES ('Cell phone', 0.0000899, 2199.12, 5);
INSERT INTO products (product_name, space, price, quantity) VALUES ('TV 55', 0.400, 4346.99, 2);
INSERT INTO products (product_name, space, price, quantity) VALUES ('TV 50', 0.290, 3999.90, 3);
INSERT INTO products (product_name, space, price, quantity) VALUES ('TV 42', 0.200, 2999.00, 4);
INSERT INTO products (product_name, space, price, quantity) VALUES ('Notebook A', 0.00350, 2499.90, 1);
INSERT INTO products (product_name, space, price, quantity) VALUES ('Ventilador', 0.496, 199.90, 10);
INSERT INTO products (product_name, space, price, quantity) VALUES ('Microwave A', 0.0424, 308.66, 2);
INSERT INTO products (product_name, space, price, quantity) VALUES ('Microwave B', 0.0544, 429.90, 5);
INSERT INTO products (product_name, space, price, quantity) VALUES ('Microwave C', 0.0319, 299.29, 3);
INSERT INTO products (product_name, space, price, quantity) VALUES ('Refrigerator B', 0.635, 849.00, 2);
INSERT INTO products (product_name, space, price, quantity) VALUES ('Refrigerator C', 0.870, 1199.89, 6);
INSERT INTO products (product_name, space, price, quantity) VALUES ('Notebook B', 0.498, 1999.90, 2);
INSERT INTO products (product_name, space, price, quantity) VALUES ('Notebook C', 0.527, 3999.00, 1);