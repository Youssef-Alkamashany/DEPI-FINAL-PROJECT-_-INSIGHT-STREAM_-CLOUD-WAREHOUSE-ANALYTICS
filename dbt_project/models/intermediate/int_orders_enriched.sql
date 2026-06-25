with orders as (
    select * from {{ ref('stg_orders') }}
),
items as (
    select * from {{ ref('stg_order_items') }}
),
products as (
    select * from {{ ref('stg_products') }}
),
customers as (
    select * from {{ ref('stg_customers') }}
),
payments as (
    select
        order_id,
        sum(payment_value) as total_payment_value
    from {{ ref('stg_payments') }}
    group by order_id
)

select
    o.order_id,
    o.customer_id,
    c.customer_state,
    o.order_status,
    o.order_purchase_timestamp,
    o.order_delivered_customer_date,
    o.order_estimated_delivery_date,
    i.product_id,
    p.product_category_name,
    i.price,
    i.freight_value,
    pay.total_payment_value
from orders o
left join items i on o.order_id = i.order_id
left join products p on i.product_id = p.product_id
left join customers c on o.customer_id = c.customer_id
left join payments pay on o.order_id = pay.order_id
