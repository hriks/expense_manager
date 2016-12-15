Commands for Postgres

sudo -i -u postgres
psql
CREATE DATABASE Database_Name
CREATE TABLE Table_Name (USERID TEXT UNIQUE   NOT NULL  REFERENCES  LOGS(USERID),
							CATAGORIES  TEXT  UNIQUE    NOT NULL,
							PRICE       INT    NOT NULL,
							DESCRIPTION TEXT );
SELECT * FROM Table_Name
SELECT PRICES FORM Table_Name
TRUNCATE TABLE LOGS
INSERT INTO LOGS(USERID,NAME,EMAIL,PASSWORD) VALUES('hriks', 'Amit kumar Gupta', 'hriks@outlook.com', 'hriks');


