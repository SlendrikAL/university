DROP TABLE IF EXISTS 'shop';
DROP TABLE IF EXISTS 'product';
DROP TABLE IF EXISTS 'warehouse';
DROP TABLE IF EXISTS 'worker';
CREATE TABLE shop(
  id INT PRIMARY KEY,
  name VARCHAR(255) UNIQUE,
  balance FLOAT NOT NULL);
INSERT INTO 'shop' VALUES(1,'пятёрочка',31);
INSERT INTO 'shop' VALUES(2,'перекрёсток',133);
CREATE TABLE product(
  id INT PRIMARY KEY,
  name VARCHAR(255) UNIQUE,
  price FLOAT NOT NULL);
INSERT INTO 'product' VALUES(1,'молоко',100);
INSERT INTO 'product' VALUES(2,'хлеб',25);
INSERT INTO 'product' VALUES(3,'сметана',10);
CREATE TABLE warehouse(
  shop_id INT REFERENCES shop(id),
  product_id INT REFERENCEs product(id),
  quantity INT NOT NULL,
  PRIMARY KEY (shop_id, product_id));
INSERT INTO 'warehouse' VALUES(1,1,20);
INSERT INTO 'warehouse' VALUES(1,2,10);
INSERT INTO 'warehouse' VALUES(2,3,30);
CREATE TABLE worker (
	worker_id INTEGER PRIMARY KEY,
	shop_id INTEGER REFERENCES product (id),
	name VARCHAR(255),
	salary INTEGER NOT NULL,
	position VARCHAR(255));
INSERT INTO 'worker' VALUES(1,1,'Алекс Джонсон',20000,'Кассир');
INSERT INTO 'worker' VALUES(2,1,'Иван Камышин',30000,'Сортировщик');
INSERT INTO 'worker' VALUES(3,2,'Павел Покрышкин',60000,'Директор');
INSERT INTO 'worker' VALUES(4,2,'Антон Гномов',15000,'Уборщик');
INSERT INTO 'worker' VALUES(5,2,'Артемий Шпалкин',20000,'Кассир');
INSERT INTO 'worker' VALUES(6,1,'Александр Походкин',60000,'Директор');
