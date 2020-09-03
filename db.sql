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
  idbarcode VARCHAR(100) NOT NULL
);

CREATE TABLE products (
  idbarcode VARCHAR(100) NOT NULL UNIQUE,
  productname VARCHAR(200) NOT NULL,
  description VARCHAR(800),
  offlink VARCHAR(1000),
  store VARCHAR(200),
  nutritiongrade VARCHAR(1),
  bio TINYINT,
  PRIMARY KEY (idbarcode)
);

CREATE TABLE substitutes (
  idboth INT NOT NULL UNIQUE AUTO_INCREMENT,
  idbarcode VARCHAR(100) NOT NULL,
  idsubstitute VARCHAR(100) NOT NULL,
  PRIMARY KEY (idboth)
);

ALTER TABLE categoryproduct
ADD CONSTRAINT fk_idcategory
FOREIGN KEY (idcategory)
REFERENCES categories(idcategory);

ALTER TABLE categoryproduct
ADD CONSTRAINT fk_idproductcat
FOREIGN KEY (idbarcode)
REFERENCES products(idbarcode);

ALTER TABLE substitutes
ADD CONSTRAINT fk_idsub
FOREIGN KEY (idsubstitute)
REFERENCES products (idbarcode);

ALTER TABLE substitutes
ADD CONSTRAINT fk_idprod
FOREIGN KEY (idbarcode)
REFERENCES products (idbarcode);
