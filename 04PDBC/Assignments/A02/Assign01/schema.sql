CREATE DATABASE if NOT EXISTS OnlineShoppingDB;

use OnlineShoppingDB;

CREATE TABLE if NOT EXISTS customer_order_pdbc(
    customer_id INT primary key,
    customer_name varchar(60),
    city varchar(40),
    email varchar(80)
);

CREATE TABLE if NOT EXISTS
product_order_pdbc(
    product_id INT primary key,
    product_name varchar(80),
    category varchar(40),
    price decimal(10,2),
    stock int
);

CREATE TABLE if NOT EXISTS
customer_order_details(
    order_id INT primary key,
    customer_id INT ,
    product_id int,
    quantity int,
    order_status varchar(40),

    constraint fk_customerOrder_customer
    foreign key (customer_id)
    references customer_order_pdbc(customer_id),

    constraint fk_customerOrder_product
    foreign key (product_id)
    references
    product_order_pdbc(product_id)
);

show tables;

desc customer_order_pdbc;
desc product_order_pdbc;
desc customer_order_details;

