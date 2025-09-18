/*Queries para responder preguntas de negocio*/

-- ¿Cual es el total de ventas por categoria de producto?
select p.product_category, count(f.transaction_id) as total_sales
from fact_sales f
join dim_products p on f.product_fk = p.product_id
group by p.product_category
order by p.product_category;

-- ¿Cual es el gasto promedio por edad de los clientes?
select c.age, round(avg(f.total_amount)) as avg_spend
from fact_sales f
join dim_customers c on f.customer_fk = c.customer_pk
group by c.age
order by c.age;

-- ¿Cual es la cantidad total de productos vendidos por genero y categoria de producto?
select c.gender, p.product_category, sum(s.quantity) as total_quantity
from staging_retail_sales s
join dim_customers c on s.customer_id = c.customer_id
join dim_products p on s.product_category = p.product_category
group by c.gender, p.product_category
order by total_quantity desc;