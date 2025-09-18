-- Tabla de staging para guardar los datos temporalmente
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

/* TABLAS DIMENSIONALES (ESQUEMA ESTRELLA) */

-- Dimension de productos
create table if not exists dim_products (
    product_id int generated always as identity primary key,
    product_category varchar(100)
);

-- Dimension de clientes 
create table if not exists dim_customers (
    customer_pk int generated always as identity primary key,
    customer_id varchar(10) unique,
    age int,
    gender varchar(100)
);

-- Dimension de fechas
create table if not exists dim_date (
    date_id int generated always as identity primary key,
    date date,
    day int,
    month int,
    year int
);

/* TABLA DE HECHOS */
create table if not exists fact_sales (
    sales_id int generated always as identity primary key,
    transaction_id int unique,
    customer_fk int references dim_customers(customer_pk),
    product_fk int references dim_products(product_id),
    date_fk int references dim_date(date_id),
    quantity int,
    price_per_unit int,
    total_amount int
);