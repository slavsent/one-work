/*
 * Курсовой проект - БД Интернет магазина, на примере магазина по торговле одеждой 
 * Проект помогает ввести учет товара на складе, движение товра от поставщиков и продажа покупателю, поддерживать цены и вводить скидки, как сезонные так
 * и прочие. Применение БД позволит выводить продукцию, цены и скидки в определенные разделы сайты. 
 * Также проект позволяет вести учет покупателей в том числе постоянных и предоставлять им отдельные скидки.
 */


DROP DATABASE IF EXISTS internet_shop;
CREATE DATABASE internet_shop;
USE internet_shop;

-- Тип продукции
DROP TABLE IF EXISTS type_product;
CREATE TABLE type_product (
	id SERIAL PRIMARY KEY, 
    name VARCHAR(100),
    description TEXT
);

INSERT INTO type_product
  (name, description)
VALUES
  ('Обувь зимняя', 'Обувь с утеплителем'),
  ('Обувь летня', 'Сандали, сланцы и т.п.'),
  ('Обувь демисизонная', 'Прочая обувь'),
  ('Одежда', 'Одежда вся'),
  ('Акссесуары', 'Для одежды и обуви');

-- Учет скидок
DROP TABLE IF EXISTS discount;
CREATE TABLE discount (
	id SERIAL PRIMARY KEY, 
    name VARCHAR(100),
    num_discount FLOAT,
    started_at DATETIME,
    finished_at DATETIME,
    created_at DATETIME DEFAULT NOW(),
    updated_at DATETIME DEFAULT NOW() ON UPDATE NOW()
);

INSERT INTO discount
  (name, num_discount, started_at, finished_at)
VALUES
  ('Летние скидкиc 2022', 50, '2022-12-01', '2022-12-31'),
  ('Зимнии скидки 2022', 50, '2022-08-01', '2022-08-31'),
  ('Демисизонные 2022', 30, NULL, NULL),
  ('Уценка', 60, NULL, NULL),
  ('Нет', 0, NULL, NULL),
  ('Персональная 5%', 5, NULL, NULL),
  ('Персональная 10%', 10, NULL, NULL),
  ('Прочие', 10, NULL, NULL);

-- Справочник продукции с ценой и возможностью указания сегозных или иных скидок
DROP TABLE IF EXISTS product;
CREATE TABLE product (
	id SERIAL PRIMARY KEY,
	id_type BIGINT UNSIGNED NOT NULL,
	name VARCHAR(100),
    description TEXT,
    size_product VARCHAR (10),
    price FLOAT,
    id_discount BIGINT UNSIGNED DEFAULT NULL,

	FOREIGN KEY (id_type) REFERENCES type_product(id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY (id_discount) REFERENCES discount(id) ON UPDATE CASCADE ON DELETE CASCADE,
	INDEX name_size_idx(name, size_product)
);

INSERT INTO product
  (id_type, name, description, size_product, price, id_discount)
VALUES
  (1, 'Ботинки скороход', 'Россия', 42, 1000, 5),
  (1, 'Ботинки скороход', 'Россия', 43, 1000, 5),
  (1, 'Ботинки скороход', 'Россия', 44, 1000, 5),
  (1, 'Ботинки LOYD', 'Германия', 41, 5000, 5),
  (1, 'Ботинки LOYD', 'Германия', 42, 5000, 5),
  (1, 'Ботинки LOYD', 'Германия', 44, 5000, 5),
  (4, 'Пальто', 'Германия', 'L', 11000, 5),
  (4, 'Брюки', 'Россия', 'L', 8000, 4),
  (4, 'Платье', 'Италия', 'S', 21000, 6),
  (5, 'Носки', 'Россия', '42-44', 250, 5),
  (5, 'Шнурки', 'Россия', '100', 110, 6);


-- Учет продукции на складе
DROP TABLE IF EXISTS storehouse;
CREATE TABLE storehouse (
	id_product SERIAL PRIMARY KEY,
	quantity INT,
	cost FLOAT COMMENT 'Стоимость товара на складе',
		
	FOREIGN KEY (id_product) REFERENCES product(id) ON UPDATE CASCADE ON DELETE CASCADE
);

INSERT INTO storehouse
  (id_product, quantity, cost)
VALUES
  (1, 3, 2400),
  (2, 8, 8000),
  (3, 04, 0),
  (4, 2, 6000),
  (5, 10, 40000),
  (6, 5, 15000),
  (7, 4, 36000),
  (8, 7, 6000),
  (9, 7, 105000),
  (10, 12, 1500),
  (11, 12, 600);
 
-- Учет поставщиков
DROP TABLE IF EXISTS supplier;
CREATE TABLE supplier (
	id SERIAL PRIMARY KEY, 
    name VARCHAR(200),
    adress TEXT,
    payment_data TEXT COMMENT 'Банковские реквезиты',
    contact_name VARCHAR (100) COMMENT 'Лицо для контактов',
    phone VARCHAR(200),
    email VARCHAR(200)
) COMMENT 'Поставщики';

INSERT INTO supplier
  (name, adress, payment_data, contact_name, phone, email)
VALUES
  ('Нет' , NULL, NULL, NULL, NULL, NULL), -- Отсутствие поставщика для прочих операций
  ('ООО Поставщик 1' , 'Москва, Кировоградский пер 1', '56456356745684 в Сбербанке', 'Журавлев С.', 74957002010, 'abc@mail.ru'),
  ('ООО Поставщик 2' , 'Москва, Тверская 24', '1234123454566 в Сбербанке', 'Сидоров М.', 74958005011, 'abc1@mail.ru'),
  ('ООО Поставщик 3' , 'Москва, Кутузовский пр-т 8', '987547354223 в Сбербанке', 'Иванов К.', 74954564444, 'abc2@mail.ru'),
  ('ООО Поставщик 4' , 'Казань, Ленина 4', '12353452345234 в Сбербанке', 'Гузеев У.', 79064833855, 'abc3@mail.ru'),
  ('ООО Поставщик 5' , 'Новосибирск, Московский буль. 7', '6346734573567 в ВТБ', 'Абрамов И.', 79105559999, 'abc4@mail.ru');

-- Учет покупателей
DROP TABLE IF EXISTS buyer;
CREATE TABLE buyer (
	id SERIAL PRIMARY KEY, 
    name VARCHAR(200),
    login_name VARCHAR(20) DEFAULT NULL,
    password_hash varchar(100) DEFAULT NULL,
    adress TEXT,
    phone VARCHAR(200),
    email VARCHAR(200),
    bithday DATE
);

INSERT INTO buyer
  (name, adress, phone, email, bithday, login_name, password_hash)
VALUES
  ('Нет' , NULL, NULL, NULL, NULL, NULL, NULL), -- Отсутствие покупателя для прочих операций
  ('Покупатель 1' , 'Москва, Рублевское ш. 5, кв 10',  79104004001, 'buy1@mail.ru', '1970-12-05', NULL, NULL),
  ('Покупатель 2' , 'Москва, Рублевское ш. 10',  79104004002, 'buy2@mail.ru', '1983-05-08', NULL, NULL),
  ('Покупатель 3' , 'Москва, Рублевское ш. 5, кв 12',  79104004003, 'buy3@mail.ru', '1992-08-11', 'user1', 'dfgdfg'),
  ('Покупатель 4' , 'Москва, Рублевское ш. 5, кв 15',  79104004004, 'buy4@mail.ru', '1977-03-21', 'user2', 'ererte'),
  ('Покупатель 5' , 'Москва, Рублевское ш. 8',  79104004005, 'buy5@mail.ru', '1969-09-10', NULL, NULL);

-- Учет транзакций по поставкам продукции
DROP TABLE IF EXISTS coming_transactions;
CREATE TABLE coming_transactions (
	id SERIAL PRIMARY KEY,
	data_transaction DATETIME DEFAULT NOW(),
	id_product BIGINT UNSIGNED NOT NULL,
	quantity INT,
	price FLOAT,
	cost FLOAT AS (quantity * price),
	id_supplier BIGINT UNSIGNED NOT NULL,
	status VARCHAR(100),

	FOREIGN KEY (id_product) REFERENCES product(id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY (id_supplier) REFERENCES supplier(id) ON UPDATE CASCADE ON DELETE CASCADE
);

INSERT INTO coming_transactions
  (data_transaction, id_product, quantity, price, id_supplier, status)
VALUES
  ('2022-04-22' , 1,  10, 700, 2, 'Оплачен, не поставлен'),
  ('2022-04-30' , 4,  4, 3000, 3, 'Ожидает поставки'),
  ('2022-05-29' , 3,  7, 700, 2, 'Исполнен'),
  ('2022-05-29' , 6,  12, 2800, 3, 'Исполнен'),
  ('2022-06-05' , 6,  5, 2800, 3, 'Ожидает поставки'),
  ('2022-05-30' , 5,  4, 3000, 3, 'Ожидает поставки'),
  ('2022-05-30' , 6,  4, 3000, 3, 'Ожидает поставки'),
  ('2022-06-10' , 7,  4, 30000, 4, 'На оплате'),
  ('2022-06-12' , 6,  4, 4000, 4, 'На оплате'),
  ('2022-06-15' , 8,  14, 6000, 5, 'На оплате');

-- Учет адресов доставки
DROP TABLE IF EXISTS adress_send;
CREATE TABLE adress_send (
	id SERIAL PRIMARY KEY,
	id_buyer BIGINT UNSIGNED,
	adress_send VARCHAR(150),
	
	FOREIGN KEY (id_buyer) REFERENCES buyer(id) ON UPDATE CASCADE ON DELETE CASCADE
);

INSERT INTO adress_send
  (id_buyer, adress_send)
VALUES
  (1, 'Самовывоз'),
  (2, 'Москва, Рублевское ш. 5, кв 10'),
  (3, 'Москва, Рублевское ш. 10'),
  (4, 'Москва, Рублевское ш. 5, кв 12'),
  (4, 'Москва, Кмевская 7'),
  (5, 'Москва, Тверская 8'),
  (6, 'Москва, Рублевское ш. 8');

-- Учет продаж
DROP TABLE IF EXISTS sell_transactions;
CREATE TABLE sell_transactions (
	id SERIAL PRIMARY KEY,
	data_transaction DATETIME DEFAULT NOW(),
	id_product BIGINT UNSIGNED NOT NULL,
	quantity INT,
	id_discount BIGINT UNSIGNED NOT NULL COMMENT 'Дополнительная скидка, например Персональная',
	cost FLOAT,
	id_buyer BIGINT UNSIGNED NOT NULL,
	id_adress_send BIGINT UNSIGNED NOT NULL,
	status VARCHAR(100),

	FOREIGN KEY (id_product) REFERENCES product(id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY (id_discount) REFERENCES discount(id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY (id_buyer) REFERENCES buyer(id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY (id_adress_send) REFERENCES adress_send(id) ON UPDATE CASCADE ON DELETE CASCADE
);


INSERT INTO sell_transactions
  (data_transaction, id_product, quantity, id_discount, cost, id_buyer, id_adress_send, status)
VALUES
  ('2022-05-28' , 2,  2, 5, 2000, 2, 2, 'Исполнен'),
  ('2022-05-28' , 5,  1, 5, 5000, 3, 3, 'Оплачен,  в доставке'),
  ('2022-03-28' , 4,  1, 5, 5000, 3, 3, 'Создан'),
  ('2022-02-28' , 5,  1, 5, 5000, 3, 3, 'Создан'),
  ('2022-05-29' , 3,  1, 5, 1000, 4, 5,'Не оплачен, в доставке'),
  ('2022-05-29' , 5,  1, 5, 1000, 4, 5,'Не оплачен, в доставке'),
  ('2022-05-29' , 7,  1, 5, 11000, 5, 6, 'Оплачен, ожидает передачи в доставку'),
  ('2022-05-30' , 8,  1, 6, 72000, 6, 7, 'Создан');

-- Учет проччих транзакций по приходу и расходу продукции
DROP TABLE IF EXISTS etc_transactions;
CREATE TABLE etc_transactions (
	id SERIAL PRIMARY KEY,
	data_transaction DATETIME DEFAULT NOW(),
	id_product BIGINT UNSIGNED NOT NULL,
	name_type VARCHAR(50) COMMENT 'Название операции',
	quantity INT,
	price FLOAT,
	cost FLOAT AS (quantity * price),
	id_buyer BIGINT UNSIGNED,
	id_supplier BIGINT UNSIGNED,
	status VARCHAR(100),
	
	FOREIGN KEY (id_product) REFERENCES product(id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY (id_supplier) REFERENCES supplier(id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY (id_buyer) REFERENCES buyer(id) ON UPDATE CASCADE ON DELETE CASCADE
);

INSERT INTO etc_transactions
  (data_transaction, id_product, name_type, quantity, price, id_buyer, id_supplier, status)
VALUES
  ('2022-05-27' , 1, 'Возврат товара', 1, 1000, 2, 1, 'Исполнен'),
  ('2022-05-27' , 1, 'Брак на уничтожение', 1, 500, 1, 1, 'На уничтожении'),
  ('2022-05-28' , 3, 'Брак в поставке', 3, 2100, 1, 2,'Возврат поставщику'),
  ('2022-05-28' , 7, 'Возврат товара', 1, 11000, 4, 1, 'Ожидает возврата средств'),
  ('2022-05-29' , 8, 'Возврат товара', 1, 7200, 5, 1, 'Создан');


 -- Получение данных с БД по товарам по категориям
 SELECT 
 	(SELECT name FROM type_product WHERE id = id_type) AS category,
 	name,
 	description,
 	size_product,
 	price,
 	(SELECT name FROM discount WHERE id = id_discount) AS discont,
 	(SELECT num_discount FROM discount WHERE id = id_discount) AS num_discount
 FROM product
 ORDER BY id_type;
 	
 -- Что покупал определенный покупатель в течении последних двух месяцев
SELECT 
	(SELECT name FROM buyer WHERE id = id_buyer) AS buyer,
	(SELECT name FROM product WHERE id = id_product) AS product,
	data_transaction
FROM sell_transactions
WHERE data_transaction > date_sub(NOW(), INTERVAL 2 MONTH)
ORDER BY data_transaction;
 
-- Определить покупателя который сделал максимальное количество покупок за месяц
SELECT 
	(SELECT name FROM buyer WHERE id = id_buyer) AS buyer,
	COUNT(*) as sum_buyes
FROM sell_transactions
GROUP BY id_buyer, data_transaction
HAVING id_buyer != 1 AND data_transaction > date_sub(NOW(), INTERVAL 1 MONTH)
ORDER BY sum_buyes DESC
LIMIT 1;
 
--  заказы которые ожидают поставки

SELECT 
	p.name as product_name,
	ct.data_transaction as data_transaction,
	ct.price as price,
	ct.cost as cost,
	s.name as seller,
	ct.status as status 
FROM coming_transactions ct 
JOIN product p ON ct.id_product = p.id 
JOIN supplier s ON ct.id_supplier = s.id 
WHERE status = 'Ожидает поставки'
ORDER BY ct.id_supplier;

-- продукция по уцененки
SELECT
	tp.name as type_product,
	p.name as name_product,
	p.size_product as size_product,
	p.price as price,
	d.name as discount
FROM product p 
LEFT JOIN type_product tp ON p.id_type = tp.id 
JOIN discount d ON p.id_discount = d.id 
WHERE d.name = 'Уценка'
ORDER BY p.id_type;
 
-- адресса доставки определенного покупателя

SELECT 
	b.name as buyer,
	as2.adress_send as adress
FROM adress_send as2 
JOIN buyer b ON as2.id_buyer = b.id 
WHERE b.id = 3;

 -- представление: выбор поставщиков название, контактное лицо и телефон
 CREATE OR REPLACE VIEW supplier_data (name, contact, phone) AS 
 (SELECT name, contact_name, phone FROM supplier
 WHERE name != 'Нет'
 ORDER BY name);

SELECT * FROM supplier_data;
 
 (data_transaction, id_product, quantity, id_discount, cost, id_buyer, id_adress_send, status)
 p.name as product_name,
	ct.data_transaction as data_transaction,
	ct.price as price,
	ct.cost as cost,
	s.name as seller,
	ct.status as status 
FROM coming_transactions ct 
JOIN product p ON ct.id_product = p.id 
JOIN supplier s ON ct.id_supplier = s.id 
 
 -- представление: не исполненые продажи
CREATE OR REPLACE VIEW sell_data_on (data_transaction, buyer, product, quantity, cost, status) AS 
 (SELECT st.data_transaction, b.name, p.name, st.quantity, st.cost, st.status FROM sell_transactions st
 JOIN product p ON st.id_product = p.id 
 JOIN buyer b ON st.id_buyer = b.id 
 WHERE st.status != 'Исполнен'
 ORDER BY st.data_transaction);

SELECT * FROM sell_data_on;
 
 
 -- тригеры на вставку и изменения цены в продажах


DELIMITER //
DROP TRIGGER IF EXISTS check_sell_transactions_insert//
CREATE TRIGGER check_sell_transactions_insert BEFORE INSERT ON sell_transactions
FOR EACH ROW 
BEGIN
	
	DECLARE price_new BIGINT;
	DECLARE disc_1 FLOAT;
	DECLARE disc_2 FLOAT;
	SET price_new = (SELECT p.price FROM product p WHERE p.id = NEW.id_product);
	SET disc_1 = (SELECT d.num_discount FROM discount d WHERE d.id = NEW.id_discount);
	SET disc_2 = (SELECT d.num_discount FROM product p JOIN discount d ON p.id_discount = d.id WHERE p.id = NEW.id_product);
	IF NEW.quantity IS NOT NULL 
	THEN  
	SET NEW.cost = NEW.quantity * price_new * (1-disc_1/100) * (1-disc_1/100);
	ELSE SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'INSERT canceled quantity is NULL';
	END IF;
END// 

DROP TRIGGER IF EXISTS check_sell_transactions_update//
CREATE TRIGGER check_sell_transactions_update BEFORE UPDATE ON sell_transactions 
FOR EACH ROW 
BEGIN 
	
	DECLARE price_new BIGINT;
	DECLARE disc_1 FLOAT;
	DECLARE disc_2 FLOAT;
	SET price_new = (SELECT p.price FROM product p WHERE p.id = NEW.id_product);
	SET disc_1 = (SELECT d.num_discount FROM discount d WHERE d.id = NEW.id_discount);
	SET disc_2 = (SELECT d.num_discount FROM product p JOIN discount d ON p.id_discount = d.id WHERE p.id = NEW.id_product);
	IF NEW.quantity IS NOT NULL 
	THEN 
	SET NEW.cost = NEW.quantity * price_new * (1-disc_1/100) * (1-disc_1/100);
	ELSE SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'UPDATE canceled quantity is NULL';
	END IF;
	
END//
 
DELIMITER ;
 
INSERT INTO sell_transactions
  (data_transaction, id_product, quantity, id_discount, id_buyer, id_adress_send, status)
VALUES
  ('2022-05-28' , 2,  2, 6, 2, 2, 'Исполнен'); 
 
 UPDATE sell_transactions
 	SET quantity = 3
 	WHERE id = 7;
 
 -- тригеры изменения остатка на складе при вставке и изменениях  в продажах 
 
DELIMITER //
DROP TRIGGER IF EXISTS check_storehouse_sell_transactions_insert//
CREATE TRIGGER check_storehouse_sell_transactions_insert AFTER INSERT ON sell_transactions
FOR EACH ROW 
BEGIN
	DECLARE quantity_ex INT;
	DECLARE coast_ex FLOAT;
	SET quantity_ex = (SELECT s.quantity FROM storehouse s WHERE s.id_product = NEW.id_product);
	SET coast_ex = (SELECT s.cost FROM storehouse s WHERE s.id_product = NEW.id_product);
	IF NEW.quantity IS NOT NULL 
	THEN
	UPDATE storehouse s
	SET s.quantity = quantity_ex - NEW.quantity,
	s.cost = coast_ex - coast_ex/quantity_ex*NEW.quantity
	WHERE 
	s.id_product = NEW.id_product;
	ELSE SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'INSERT canceled quantity is NULL';
	END IF;
END// 

DROP TRIGGER IF EXISTS check_storehouse_sell_transactions_update//
CREATE TRIGGER check_storehouse_sell_transactions_update AFTER UPDATE ON sell_transactions 
FOR EACH ROW 
BEGIN 
	DECLARE quantity_ex INT;
	DECLARE coast_ex FLOAT;
	SET quantity_ex = (SELECT s.quantity FROM storehouse s WHERE s.id_product = NEW.id_product);
	SET coast_ex = (SELECT s.cost FROM storehouse s WHERE s.id_product = NEW.id_product);
	IF NEW.quantity IS NOT NULL AND NEW.quantity != OLD.quantity
	THEN
	UPDATE storehouse s
	SET s.quantity = quantity_ex - NEW.quantity + OLD.quantity,
	s.cost = coast_ex + coast_ex/quantity_ex*(OLD.quantity - NEW.quantity)
	WHERE 
	s.id_product = NEW.id_product;
	ELSEIF NEW.quantity IS NULL
	THEN
	SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'INSERT canceled quantity is NULL';
	END IF;
END//

DROP TRIGGER IF EXISTS check_storehouse_sell_transactions_del//
CREATE TRIGGER check_storehouse_sell_transactions_del AFTER DELETE ON sell_transactions
FOR EACH ROW 
BEGIN
	DECLARE quantity_ex INT;
	DECLARE coast_ex FLOAT;
	SET quantity_ex = (SELECT s.quantity FROM storehouse s WHERE s.id_product = OLD.id_product);
	SET coast_ex = (SELECT s.cost FROM storehouse s WHERE s.id_product = OLD.id_product);
	UPDATE storehouse s
	SET s.quantity = quantity_ex + OLD.quantity,
	s.cost = coast_ex + coast_ex/quantity_ex*OLD.quantity
	WHERE 
	s.id_product = OLD.id_product;
	
END// 

 
DELIMITER ;

 
INSERT INTO sell_transactions
  (data_transaction, id_product, quantity, id_discount, id_buyer, id_adress_send, status)
VALUES
  ('2022-05-28' , 5,  2, 6, 2, 2, 'Исполнен'); 
 
 UPDATE sell_transactions
 	SET quantity = 3
 	WHERE id = 9;
 
 -- процедура повторения исполненых заказов поставки определенного поставщика
 
DELIMITER //
DROP PROCEDURE IF EXISTS add_coming_transactions//
CREATE PROCEDURE add_coming_transactions(IN id_sup BIGINT)
BEGIN
	IF id_sup > 0 THEN
		INSERT INTO coming_transactions (data_transaction, id_product, quantity, price, id_supplier, status)
		(SELECT DISTINCT NOW(), id_product, quantity, price, id_supplier, 'Новый' FROM coming_transactions ct 
		WHERE id_supplier = id_sup AND status = 'Исполнен'
		ORDER BY data_transaction DESC);
	END IF;
END//
DELIMITER ;

CALL add_coming_transactions(2);

INSERT INTO coming_transactions
  (data_transaction, id_product, quantity, price, id_supplier, status)
VALUES
  ('2022-05-22' , 2,  10, 700, 2, 'Исполнен'),
  ('2022-05-30' , 4,  4, 3000, 2, 'Исполнен'),
  ('2022-05-29' , 3,  7, 700, 2, 'Исполнен');

-- процедура удаления заказов - продажи со сроком создания больше оперделенного количества дней и статусом Создан
 
DELIMITER //
DROP PROCEDURE IF EXISTS del_sell_transactions//
CREATE PROCEDURE del_sell_transactions(IN num_day INT)
BEGIN
	IF num_day > o THEN
		DELETE FROM sell_transactions 
		WHERE data_transaction < date_sub(NOW(), INTERVAL num_day DAY) AND status = 'Создан';
	END IF;
	
END//
DELIMITER ;

INSERT INTO sell_transactions
  (data_transaction, id_product, quantity, id_discount, cost, id_buyer, id_adress_send, status)
VALUES
  ('2022-03-28' , 4,  1, 5, 5000, 3, 3, 'Создан'),
  ('2022-02-28' , 5,  1, 5, 5000, 3, 3, 'Создан');

CALL del_sell_transactions(31);
 
 
 
 
 
 
 