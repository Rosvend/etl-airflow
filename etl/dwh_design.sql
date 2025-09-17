create table if not exists staging_retail_sales (
    transaction_id int primary key,
    Date date,
    customer_id varchar(10),
    age int,
    gender text,
    product_category text,
    quantity int,
    price_per_unit int,
    total_amount int
);

create table if not exists dim_products (
    product_id int primary key,
    product_category varchar(100)
);

create table if not exists dim_customers (
    customer_id int primary key,
    age int,
    gender varchar(100)
);

create table if not exists dim_date (
    date_id int primary key,
    date date,
    day int,
    month int,
    year int
);

insert into dim_products (product_id, product_category)
select distinct
    row_number() over (order by product_category) as product_id,
    product_category
from staging_retail_sales;