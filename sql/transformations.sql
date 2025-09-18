/*Insercion de datos en la tabla dim_products*/
insert into dim_products (product_category)
select distinct s.product_category
from staging_retail_sales s
where not exists (
    select 1
    from dim_products d
    where d.product_category = s.product_category
);

/*Insercion de datos en la tabla dim_customers*/
insert into dim_customers (customer_id, age, gender)
select distinct s.customer_id, s.age, s.gender
from staging_retail_sales s
where not exists (
    select 1
    from dim_customers d
    where d.customer_id = s.customer_id
);

/*Insercion de datos en la tabla dim_date*/
insert into dim_date (date, day, month, year)
select distinct
    s.date,
    extract(day from s.date) as day,
    extract(month from s.date) as month,
    extract(year from s.date) as year
from staging_retail_sales s
where not exists (
    select 1
    from dim_date d
    where d.date = s.date
);


/*Insercion de datos en la tabla fact_sales*/
insert into fact_sales (transaction_id, customer_fk, product_fk, date_fk, quantity, price_per_unit, total_amount)
select
    s.transaction_id,
    c.customer_pk,
    p.product_id,
    d.date_id,
    s.quantity,
    s.price_per_unit,
    s.total_amount
from staging_retail_sales s
join dim_customers c on s.customer_id = c.customer_id
join dim_products p on s.product_category = p.product_category
join dim_date d on s.date = d.date
where not exists (
    select 1
    from fact_sales f
    where f.transaction_id = s.transaction_id
);


--Limpieza de la tabla staging_retail_sales
truncate table staging_retail_sales;