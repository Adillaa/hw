-- CREATE TABLE phones(
--     id SERIAL PRIMARY KEY,
--     name VARCHAR(30),
--     price INT);
-- INSERT INTO phones(name, price) VALUES ('Iphone', 100);
-- ALTER TABLE phones ADD country VARCHAR(18);
-- INSERT INTO phones(name, price, country) VALUES('Samsung', 120, 'Korea')
-- INSERT INTO phones(name, price, country) VALUES('nokia',1000,'kg')
-- INSERT INTO phones(name, price, country) VALUES('MI',1,'uzbekistan')
-- INSERT INTO phones(name, price, country) VALUES('Google',0,'USA')

-- CREATE TABLE cars(
--     id SERIAL PRIMARY KEY,
--     name VARCHAR(20),
--     price INT DEFAULT 300);

-- INSERT INTO cars(name,price) VALUES('MB', 1000)
-- ALTER TABLE cars ADD country VARCHAR(24);
-- INSERT INTO cars(name, price, country) VALUES('audi',300,'germany')
-- INSERT INTO cars(name, price, country) VALUES('BMW', 12000,'Germany')
-- INSERT INTO cars(name, price, country) VALUES('Tulpar', 10000000,'KG')
-- UPDATE cars SET country='Germany' WHERE name='MB';
-- SELECT * FROM cars;
-- SELECT * FROM phones;

