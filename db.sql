DROP DATABASE IF EXISTS pur_beurre;
CREATE DATABASE pur_beurre CHARACTER SET 'utf8';
USE pur_beurre;

CREATE TABLE categories (
  idcategory INT NOT NULL AUTO_INCREMENT UNIQUE,
  categoryname VARCHAR(100) NOT NULL UNIQUE,
  PRIMARY KEY (idcategory)
);

CREATE TABLE categoryproduct (
  idcategory INT NOT NULL ,
  idproduct INT NOT NULL
);

CREATE TABLE products (
  idproduct INT NOT NULL AUTO_INCREMENT UNIQUE,
  productname VARCHAR(200) NOT NULL,
  description VARCHAR(800),
  offlink VARCHAR(1000),
  store VARCHAR(200),
  barcode VARCHAR(100) NOT NULL UNIQUE,
  nutritiongrade VARCHAR(1),
  bio TINYINT,
  PRIMARY KEY (idproduct)
);

CREATE TABLE substitutes (
  idboth INT NOT NULL UNIQUE AUTO_INCREMENT,
  idproduct INT NOT NULL,
  idsubstitute INT NOT NULL,
  PRIMARY KEY (idboth)
);

ALTER TABLE categoryproduct
ADD CONSTRAINT fk_idcategory
FOREIGN KEY (idcategory)
REFERENCES categories(idcategory);

ALTER TABLE categoryproduct
ADD CONSTRAINT fk_idproductcat
FOREIGN KEY (idproduct)
REFERENCES products(idproduct);

ALTER TABLE substitutes
ADD CONSTRAINT fk_idsub
FOREIGN KEY (idsubstitute)
REFERENCES products (idproduct);

ALTER TABLE substitutes
ADD CONSTRAINT fk_idprod
FOREIGN KEY (idproduct)
REFERENCES products (idproduct);
