CREATE TABLE Customer (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL
);


CREATE TABLE CustomerProfile (
    id SERIAL PRIMARY KEY,
    isLoggedIn BOOLEAN DEFAULT false,
    customer_id INTEGER UNIQUE REFERENCES Customer(id)
);

INSERT INTO Customer (first_name, last_name) VALUES 
('John', 'Doe'),
('Jerome', 'Lalu'),
('Lea', 'Rive');

INSERT INTO CustomerProfile (isLoggedIn, customer_id) VALUES 
(true, (SELECT id FROM Customer WHERE first_name = 'John')),
(false, (SELECT id FROM Customer WHERE first_name = 'Jerome'));*/

-- first_name of LoggedIn customers using INNER JOIN
SELECT c.first_name
FROM Customer c
INNER JOIN CustomerProfile cp ON c.id = cp.customer_id
WHERE cp.isLoggedIn = true;

-- count not logged in 
SELECT COUNT(c.id) AS num_not_logged_in
FROM Customer c
RIGHT JOIN CustomerProfile cp ON c.id = cp.customer_id
WHERE cp.isLoggedIn IS FALSE;*/





