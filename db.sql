DROP DATABASE IF EXISTS pur_beurre;
CREATE DATABASE pur_beurre CHARACTER SET 'utf8';
USE pur_beurre;

CREATE TABLE categories (
  categoryid INT NOT NULL UNIQUE AUTO_INCREMENT,
  categoryname VARCHAR(100) NOT NULL UNIQUE,
  PRIMARY KEY (categoryname)
);

CREATE TABLE categoryproduct (
  categoryname VARCHAR(100) NOT NULL,
  idbarcode VARCHAR(100) NOT NULL
);

CREATE TABLE products (
  productid INT NOT NULL UNIQUE AUTO_INCREMENT,
  idbarcode VARCHAR(100) NOT NULL UNIQUE,
  productname VARCHAR(200) NOT NULL,
  description VARCHAR(800),
  offlink VARCHAR(1000),
  store VARCHAR(200),
  nutritiongrade VARCHAR(1),
  PRIMARY KEY (idbarcode)
);

CREATE TABLE substitutes (
  idboth INT NOT NULL UNIQUE AUTO_INCREMENT,
  idbarcode VARCHAR(100) NOT NULL,
  idsubstitute VARCHAR(100) NOT NULL,
  PRIMARY KEY (idboth)
);


ALTER TABLE substitutes
ADD CONSTRAINT fk_idsub
FOREIGN KEY (idsubstitute)
REFERENCES products (idbarcode);

ALTER TABLE substitutes
ADD CONSTRAINT fk_idprod
FOREIGN KEY (idbarcode)
REFERENCES products (idbarcode);
